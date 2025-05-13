import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error, mean_absolute_percentage_error, r2_score

def run_arima_forecast(resource_data, years_ahead=10):
    df = pd.DataFrame(resource_data).sort_values('year')
    series = df['consumption'].astype(float)

    model = ARIMA(series, order=(1, 1, 1))
    model_fit = model.fit()

    forecast = model_fit.forecast(steps=years_ahead)
    start_year = df['year'].max() + 1
    years = list(range(start_year, start_year + years_ahead))

    forecast_list = [{'ds': y, 'yhat': float(v)} for y, v in zip(years, forecast)]

    # Метрики по последним known значениям
    actual = series[-years_ahead:].values
    predicted = forecast[:len(actual)]

    rmse = mean_squared_error(actual, predicted, squared=False)
    mape = mean_absolute_percentage_error(actual, predicted)
    r2 = r2_score(actual, predicted)

    metrics = {
        'RMSE': round(rmse, 4),
        'MAPE': round(mape * 100, 2),
        'R2': round(r2, 4)
    }

    return forecast_list, metrics
