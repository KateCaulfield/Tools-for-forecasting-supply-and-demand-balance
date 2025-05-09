from prophet import Prophet
import pandas as pd


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
    return result.to_dict(orient='records')
