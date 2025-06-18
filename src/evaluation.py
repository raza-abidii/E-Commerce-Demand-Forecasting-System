from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error
import pandas as pd

X_train = np.array([[1], [2], [3], [4], [5]])
y_train = np.array([100, 120, 130, 140, 150])
X_test = np.array([[6], [7], [8]])
y_true = np.array([160, 170, 180])


def calculate_metrics(y_true, y_pred):
    from sklearn.metrics import r2_score

    mse = mean_squared_error(y_true, y_pred)
    mae = mean_absolute_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)

    return {
        'Mean Squared Error': mse,
        'Mean Absolute Error': mae,
        'R-squared': r2
    }


def plot_results(y_true, y_pred):
    import matplotlib.pyplot as plt
    plt.ion() 

    plt.figure(figsize=(10, 5))
    plt.plot(y_true, label='Actual Demand', color='blue')
    plt.plot(y_pred, label='Predicted Demand', color='orange')
    plt.title('Demand Forecasting Results')
    plt.xlabel('Time')
    plt.ylabel('Demand')
    plt.legend()
    plt.show()


def evaluate(model, df: pd.DataFrame):
    """
    Evaluates the model on the provided DataFrame.
    Assumes 'date' and 'demand' columns exist.
    """
    X = df['date'].map(pd.Timestamp.toordinal).values.reshape(-1, 1)
    y_true = df['demand'].values
    y_pred = model.predict(X)
    mae = mean_absolute_error(y_true, y_pred)
    mse = mean_squared_error(y_true, y_pred)
    return {
        "Mean Absolute Error": mae,
        "Mean Squared Error": mse
    }