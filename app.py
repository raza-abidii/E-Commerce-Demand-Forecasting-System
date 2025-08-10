import streamlit as st
import pandas as pd
import plotly.graph_objs as go
from src import data_preprocessing, forecasting_model, evaluation, utils

st.set_page_config(page_title="E-Commerce Demand Forecasting", layout="wide")
st.title("📈 E-Commerce Demand Forecasting System")

st.sidebar.header("Step 1: Upload Data")
uploaded_file = st.sidebar.file_uploader("Upload your sales CSV", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("Raw Data Preview")
    st.dataframe(df.head())
    st.session_state['raw_df'] = df
    st.success("Data uploaded successfully!")
    
    #Select Product/Category
    filter_col = None
    for col in df.columns:
        if col.lower() in ['product', 'item', 'category', 'product_name', 'item_name']:
            filter_col = col
            break

    selected_value = None
    if filter_col:
        unique_values = df[filter_col].dropna().unique()
        selected_value = st.sidebar.selectbox(
            f"Select {filter_col} for forecasting", unique_values
        )
        df = df[df[filter_col] == selected_value]
        st.write(f"Forecasting for **{filter_col}: {selected_value}**")
    else:
        st.info("No product/category column found. Forecasting on all data.")

    #Preprocess Data
    st.sidebar.header("Step 2: Preprocess Data")
    if st.sidebar.button("Preprocess Data"):
        processed_df = data_preprocessing.preprocess(df)
        st.session_state['processed_df'] = processed_df
        st.success("Data preprocessed successfully!")
        st.subheader("Processed Data Preview")
        st.dataframe(processed_df.head())

    #Train Model
    if 'processed_df' in st.session_state:
        st.sidebar.header("Step 3: Train Model")
        if st.sidebar.button("Train Model"):
            model = forecasting_model.train(st.session_state['processed_df'])
            st.session_state['model'] = model
            st.success("Model trained successfully!")

    #Forecast and Plot
    if 'model' in st.session_state and 'processed_df' in st.session_state:
        st.sidebar.header("Step 4: Forecast")
        periods = st.sidebar.number_input("Forecast periods (days)", min_value=1, max_value=365, value=30)
        if st.sidebar.button("Generate Forecast"):
            forecast_df = forecasting_model.forecast(
                st.session_state['model'],
                st.session_state['processed_df'],
                periods
            )
            st.success("Forecast generated!")

            #Combine historical and forecast data for plotting
            historical = st.session_state['processed_df'].copy()
            historical['Type'] = 'Historical'
            forecast = forecast_df.copy()
            forecast['Type'] = 'Forecast'
            combined = pd.concat([historical, forecast], ignore_index=True)

            #Plot
            st.subheader("Demand Forecast Visualization")
            fig = go.Figure()
            fig.add_trace(go.Scatter(
                x=historical['date'], y=historical['demand'],
                mode='lines+markers', name='Historical', line=dict(color='#00FFAA')
            ))
            fig.add_trace(go.Scatter(
                x=forecast['date'], y=forecast['demand'],
                mode='lines+markers', name='Forecast', line=dict(color='#FF2D55')
            ))
            fig.update_layout(
                xaxis_title="Date",
                yaxis_title="Demand",
                legend_title="Legend",
                template="plotly_dark",
                plot_bgcolor='#000',
                paper_bgcolor='#000',
                font=dict(color='#fff')
            )
            st.plotly_chart(fig, use_container_width=True)

            #Evaluation
            st.subheader("Model Evaluation")
            metrics = evaluation.evaluate(st.session_state['model'], st.session_state['processed_df'])
            st.json(metrics)
else:
    st.info("Please upload a CSV file to begin.")

def preprocess(df):
    if 'Date' in df.columns:
        df = df.rename(columns={'Date': 'date'})
    df['date'] = pd.to_datetime(df['date'])
    return df