import pandas as pd
import streamlit as st

def load_data(file_path):
    data = pd.read_csv("data/cleaned_retail_data.csv")
    return data


def transform_data(data):
    data['order_date'] = pd.to_datetime(data['order_date'])
    return data

def preprocess(df):
    date_col = None
    for col in df.columns:
        if col.lower() in ['date', 'order_date', 'timestamp', 'datetime']:
            date_col = col
            break
    if date_col is None:
        raise ValueError(
            "No date column found. Please ensure your data has a column named 'date', 'order_date', 'timestamp', or 'datetime'."
        )
    df = df.rename(columns={date_col: 'date'})
    df['date'] = pd.to_datetime(df['date'])

    demand_col = None
    for col in df.columns:
        if col.lower() in ['demand', 'sales', 'quantity', 'units_sold']:
            demand_col = col
            break
    if demand_col is None:
        raise ValueError(
            "No demand column found. Please ensure your data has a column named 'demand', 'sales', 'quantity', or 'units_sold'."
        )
    df = df.rename(columns={demand_col: 'demand'})

    df = df.sort_values('date')
    return df