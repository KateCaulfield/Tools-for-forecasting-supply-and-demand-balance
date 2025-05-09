import pandas as pd
from sklearn.linear_model import LinearRegression

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

    return [
        {'ds': str(year), 'yhat': float(pred)}
        for year, pred in zip(future_years, future_y)
    ]
