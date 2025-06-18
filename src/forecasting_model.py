import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
import joblib

class ForecastingModel:
    def __init__(self, model):
        self.model = model

    def train_model(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def predict(self, X_test):
        return self.model.predict(X_test)

    def save_model(self, file_path):
        joblib.dump(self.model, file_path)

    @classmethod
    def load_model(cls, file_path):
        model = joblib.load(file_path)
        return cls(model)

    def evaluate_model(self, X_test, y_true):
        y_pred = self.predict(X_test)
        print("Evaluation Metrics:")

def train(df: pd.DataFrame):
    X = df['date'].map(pd.Timestamp.toordinal).values.reshape(-1, 1)
    y = df['demand'].values
    model = LinearRegression()
    model.fit(X, y)
    return model

def forecast(model, df: pd.DataFrame, periods: int) -> pd.DataFrame:
    last_date = df['date'].max()
    future_dates = [last_date + pd.Timedelta(days=i) for i in range(1, periods + 1)]
    X_future = np.array([d.toordinal() for d in future_dates]).reshape(-1, 1)
    y_pred = model.predict(X_future)
    forecast_df = pd.DataFrame({'date': future_dates, 'demand': y_pred})
    return forecast_df
