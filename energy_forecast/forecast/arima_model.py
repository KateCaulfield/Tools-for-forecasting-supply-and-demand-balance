import pandas as pd
from statsmodels.tsa.arima.model import ARIMA


def run_arima_forecast(resource_data, years_ahead=10):
    df = pd.DataFrame(resource_data).sort_values('year')
    series = df['consumption'].astype(float)

    model = ARIMA(series, order=(1, 1, 1))
    model_fit = model.fit()

    forecast = model_fit.forecast(steps=years_ahead)
    start_year = df['year'].max() + 1
    years = list(range(start_year, start_year + years_ahead))

    return [{'ds': y, 'yhat': float(v)} for y, v in zip(years, forecast)]
