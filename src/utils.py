import pandas as pd

def create_features(df):
    """Basic feature engineering that achieved better results"""
    df = df.copy()
    
    # Time-based features
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    df['day'] = df['date'].dt.day
    df['day_of_week'] = df['date'].dt.dayofweek
    
    # Simple lag features
    df['lag_1'] = df['demand'].shift(1)
    df['lag_7'] = df['demand'].shift(7)
    df['rolling_mean_7'] = df['demand'].rolling(window=7).mean()
    
    return df

FEATURE_COLUMNS = [
    'year', 'month', 'day', 'day_of_week',
    'lag_1', 'lag_7', 'rolling_mean_7'
]