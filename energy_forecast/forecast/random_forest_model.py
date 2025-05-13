import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_percentage_error, r2_score

def run_rf_forecast(resource_data, years_ahead=10):
    df = pd.DataFrame(resource_data)
    df = df.sort_values('year')

    # Обучающая выборка
    X = df[['year', 'production', 'import_value', 'export_value']]
    y = df['consumption']

    model = RandomForestRegressor(n_estimators=100)
    model.fit(X, y)

    # Прогноз на N лет вперёд
    last = df.iloc[-1]
    future_years = [last['year'] + i for i in range(1, years_ahead + 1)]
    future_X = pd.DataFrame({
        'year': future_years,
        'production': last['production'],
        'import_value': last['import_value'],
        'export_value': last['export_value'],
    })

    preds = model.predict(future_X)
    forecast_list = [{'ds': int(y), 'yhat': float(p)} for y, p in zip(future_years, preds)]

    # Вычисление метрик (используем последние фактические значения для сравнения)
    y_true = y.tail(years_ahead).values
    y_pred = preds[:len(y_true)]

    rmse = mean_squared_error(y_true, y_pred, squared=False)
    mape = mean_absolute_percentage_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)

    metrics = {
        'RMSE': round(rmse, 4),
        'MAPE': round(mape * 100, 2),
        'R2': round(r2, 4)
    }

    return forecast_list, metrics
