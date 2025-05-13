from prophet import Prophet
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_percentage_error, r2_score

def run_prophet_forecast(resource_data, years_ahead=10):
    """
    resource_data: QuerySet или список словарей с полями 'year' и 'consumption'
    years_ahead: сколько лет вперёд прогнозировать
    """
    df = pd.DataFrame(resource_data)
    df = df[['year', 'consumption']]
    df = df.rename(columns={'year': 'ds', 'consumption': 'y'})
    df['ds'] = pd.to_datetime(df['ds'], format='%Y')

    model = Prophet(yearly_seasonality=True)
    model.fit(df)

    future = model.make_future_dataframe(periods=years_ahead, freq='Y')
    forecast = model.predict(future)

    result = forecast[['ds', 'yhat']].tail(years_ahead)
    result['ds'] = result['ds'].dt.year

    forecast_list = result.to_dict(orient='records')

    # Вычисление метрик — сравнение с последними years_ahead значениями исходного ряда
    actual = df.tail(years_ahead)['y'].values
    predicted = result['yhat'].values[:len(actual)]

    rmse = mean_squared_error(actual, predicted, squared=False)
    mape = mean_absolute_percentage_error(actual, predicted)
    r2 = r2_score(actual, predicted)

    metrics = {
        'RMSE': round(rmse, 4),
        'MAPE': round(mape * 100, 2),
        'R2': round(r2, 4)
    }

    return forecast_list, metrics
