from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np
import pandas as pd
from .utils import create_features, FEATURE_COLUMNS


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


def evaluate(model_tuple, df):
    """Evaluate model performance using consistent features"""
    model, scaler, _ = model_tuple
    
    # Create features using shared function
    df_processed = create_features(df)
    df_processed = df_processed.dropna()
    
    # Prepare features
    X = df_processed[FEATURE_COLUMNS].values
    y_true = df_processed['demand'].values
    
    # Scale features and predict
    X_scaled = scaler.transform(X)
    y_pred = model.predict(X_scaled)
    
    # Calculate metrics
    mae = mean_absolute_error(y_true, y_pred)
    mse = mean_squared_error(y_true, y_pred)
    rmse = np.sqrt(mse)
    mape = np.mean(np.abs((y_true - y_pred) / y_true)) * 100
    accuracy = 100 - mape
    
    return {
        "Mean Absolute Error": mae,
        "Root Mean Square Error": rmse,
        "R-squared Score": model.score(X_scaled, y_true),
        "MAPE": mape,
        "Forecast Accuracy": accuracy
    }