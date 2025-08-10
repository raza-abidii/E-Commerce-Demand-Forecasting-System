from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
import pandas as pd
from .utils import create_features, FEATURE_COLUMNS

def train(df: pd.DataFrame):
    """Train model with original parameters"""
    # Create features
    df_processed = create_features(df)
    df_processed = df_processed.dropna()
    
    # Prepare features
    X = df_processed[FEATURE_COLUMNS].values
    y = df_processed['demand'].values
    
    # Scale features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Train model with original parameters
    model = RandomForestRegressor(
        n_estimators=100,
        max_depth=10,
        min_samples_split=5,
        min_samples_leaf=2,
        random_state=42,
        n_jobs=-1
    )
    model.fit(X_scaled, y)
    
    return (model, scaler, FEATURE_COLUMNS)

def forecast(model_tuple, df: pd.DataFrame, periods: int) -> pd.DataFrame:
    """Generate forecasts using consistent features"""
    model, scaler, features = model_tuple
    
    # Initialize forecast dataframe
    last_date = df['date'].max()
    future_dates = [last_date + pd.Timedelta(days=i) for i in range(1, periods + 1)]
    future_df = pd.DataFrame({'date': future_dates})
    
    # Get last values for lag features
    last_demands = df['demand'].tail(7).values
    last_demand = df['demand'].iloc[-1]
    
    # Generate predictions iteratively
    predictions = []
    for i in range(periods):
        # Create temporary df with current prediction date
        temp_df = pd.DataFrame({'date': [future_dates[i]], 'demand': [last_demand]})
        
        # Add features
        temp_df = create_features(temp_df)
        
        # Update lag values
        if i == 0:
            temp_df['lag_1'] = last_demand
            temp_df['lag_7'] = df['demand'].iloc[-7] if len(df) >= 7 else last_demand
        else:
            temp_df['lag_1'] = predictions[i-1]
            temp_df['lag_7'] = df['demand'].iloc[-7+i] if i < 7 else predictions[i-7]
        
        # Scale and predict
        X_pred = temp_df[features].values
        X_pred_scaled = scaler.transform(X_pred)
        pred = model.predict(X_pred_scaled)[0]
        predictions.append(pred)
        
        # Update last demand for next iteration
        last_demand = pred
    
    return pd.DataFrame({
        'date': future_dates,
        'demand': predictions
    })
