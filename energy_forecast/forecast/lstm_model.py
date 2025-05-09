import torch
import torch.nn as nn
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

class LSTMModel(nn.Module):
    def __init__(self, input_size=1, hidden_size=50, output_size=1):
        super().__init__()
        self.lstm = nn.LSTM(input_size, hidden_size, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        out, _ = self.lstm(x)
        out = self.fc(out[:, -1, :])
        return out

def run_lstm_forecast(resource_data, years_ahead=10):
    df = pd.DataFrame(resource_data)
    df = df.sort_values('year')
    series = df['consumption'].values.astype(np.float32).reshape(-1, 1)

    # если данных слишком мало — выход
    if len(series) < 6:
        raise ValueError("Недостаточно данных для прогноза LSTM (нужно минимум 6 записей по годам)")

    scaler = MinMaxScaler()
    scaled = scaler.fit_transform(series)

    # автоподстройка длины последовательности
    seq_length = min(5, len(scaled) - 1)
    x_train, y_train = [], []

    for i in range(len(scaled) - seq_length):
        x_train.append(scaled[i:i + seq_length])
        y_train.append(scaled[i + seq_length])

    if not x_train:
        raise ValueError("Недостаточно данных после подготовки последовательностей для LSTM.")

    x_train = torch.tensor(x_train, dtype=torch.float32)  # [N, seq_length, 1]
    y_train = torch.tensor(y_train, dtype=torch.float32).squeeze()  # [N]

    model = LSTMModel()
    criterion = nn.MSELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

    model.train()
    for _ in range(200):
        optimizer.zero_grad()
        output = model(x_train)
        loss = criterion(output.squeeze(), y_train)
        loss.backward()
        optimizer.step()

    last_seq = torch.tensor(scaled[-seq_length:], dtype=torch.float32).unsqueeze(0)
    model.eval()
    preds = []
    current_year = int(df['year'].max())

    for _ in range(years_ahead):
        with torch.no_grad():
            next_pred = model(last_seq)
        preds.append(next_pred.item())
        next_pred_reshaped = next_pred.view(1, 1, 1)
        next_scaled = torch.cat((last_seq[:, 1:, :], next_pred_reshaped), dim=1)
        last_seq = next_scaled

    forecast = scaler.inverse_transform(np.array(preds).reshape(-1, 1)).flatten()
    return [
        {'ds': str(current_year + i + 1), 'yhat': float(val)}
        for i, val in enumerate(forecast)
    ]
