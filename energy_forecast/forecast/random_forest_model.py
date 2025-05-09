import pandas as pd
from sklearn.ensemble import RandomForestRegressor


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
    return [{'ds': int(y), 'yhat': float(p)} for y, p in zip(future_years, preds)]
