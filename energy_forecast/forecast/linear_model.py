import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_percentage_error, r2_score

def run_linear_regression(resource_data, years_ahead=10):
    df = pd.DataFrame(resource_data)
    df = df[df['year'].notnull()]
    df = df.sort_values('year')

    X = df[['year']]
    y = df['consumption']

    model = LinearRegression()
    model.fit(X, y)

    last_year = int(df['year'].max())
    future_years = list(range(last_year + 1, last_year + years_ahead + 1))
    future_X = pd.DataFrame({'year': future_years})
    future_y = model.predict(future_X)

    forecast_list = [
        {'ds': str(year), 'yhat': float(pred)}
        for year, pred in zip(future_years, future_y)
    ]

    # Метрики по последним фактическим точкам
    y_true = y.tail(years_ahead).values
    y_pred = future_y[:len(y_true)]

    rmse = mean_squared_error(y_true, y_pred, squared=False)
    mape = mean_absolute_percentage_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)

    metrics = {
        'RMSE': round(rmse, 4),
        'MAPE': round(mape * 100, 2),
        'R2': round(r2, 4)
    }

    return forecast_list, metrics
