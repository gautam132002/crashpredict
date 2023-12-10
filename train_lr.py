import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np

def linear_regression_predict_next_outcome(csv_path='data.csv', target_column = 'ticket'):
    data = pd.read_csv(csv_path)
    data = data.drop(['id', 'serverSeed'], axis=1)
    X = data.drop(target_column, axis=1)
    y = data[target_column]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    next_input = X.iloc[[-1]]
    next_prediction = int(np.round(model.predict(next_input)[0]))
    return next_prediction/100


next_outcome = linear_regression_predict_next_outcome()
print(f'Predicted Next Outcome: {next_outcome}')
