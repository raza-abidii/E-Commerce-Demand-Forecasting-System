# E-Commerce Demand Forecasting System – Technical Documentation

## Overview

This system forecasts demand for e-commerce products using historical sales data. It includes data preprocessing, model training, evaluation, and a modern Streamlit UI for interactive forecasting and visualization.

---

## Project Structure

```
ecommerce-demand-forecasting
├── data
│   ├── #Data for prediction
├── src
│   ├── data_preprocessing.py      # Data loading and preprocessing functions
│   ├── forecasting_model.py       # Model training and forecasting functions
│   ├── evaluation.py              # Model evaluation metrics
├── app.py                         # Streamlit UI application
├── requirements.txt               # Python dependencies
├── README.md                      # Project overview and setup
├── DOCUMENTATION.md               # (This file) Detailed codebase documentation
```

---

## Module & API Reference

### 1. `src/data_preprocessing.py`

**Purpose:**  
Standardizes and cleans raw data for modeling.

**Functions:**

#### `preprocess(df: pd.DataFrame) -> pd.DataFrame`
- **Description:**  
  Cleans and standardizes the input DataFrame.
- **Parameters:**  
  - `df`: Input DataFrame with raw data.
- **Returns:**  
  - Cleaned DataFrame with columns: `date` (datetime), `demand` (numeric), and any other columns.
- **Raises:**  
  - `ValueError` if required columns are missing.
- **Behavior:**  
  - Renames date and demand columns to standard names (`date`, `demand`).
  - Converts the `date` column to `datetime`.
  - Sorts by date.
  - Drops rows with missing values in key columns.

**Example:**
```python
import pandas as pd
from src import data_preprocessing

df = pd.read_csv("data.csv")
clean_df = data_preprocessing.preprocess(df)
```

---

### 2. `src/forecasting_model.py`

**Purpose:**  
Trains a regression model and generates demand forecasts.

**Functions:**

#### `train(df: pd.DataFrame)`
- **Description:**  
  Trains a linear regression model using date and demand.
- **Parameters:**  
  - `df`: DataFrame with `date` (datetime) and `demand` (numeric).
- **Returns:**  
  - Trained scikit-learn regression model.
- **Raises:**  
  - `KeyError` if required columns are missing.

#### `forecast(model, df: pd.DataFrame, periods: int) -> pd.DataFrame`
- **Description:**  
  Generates demand forecasts for a specified number of future periods.
- **Parameters:**  
  - `model`: Trained regression model.
  - `df`: DataFrame with historical data (`date` column).
  - `periods`: Number of future days to forecast.
- **Returns:**  
  - DataFrame with columns: `date`, `demand` (forecasted values).

**Example:**
```python
from src import forecasting_model

model = forecasting_model.train(clean_df)
future_df = forecasting_model.forecast(model, clean_df, periods=30)
```

---

### 3. `src/evaluation.py`

**Purpose:**  
Evaluates model performance using standard metrics.

**Functions:**

#### `evaluate(model, df: pd.DataFrame) -> dict`
- **Description:**  
  Evaluates the model on the provided data.
- **Parameters:**  
  - `model`: Trained regression model.
  - `df`: DataFrame with `date` and `demand`.
- **Returns:**  
  - Dictionary with evaluation metrics:  
    - `"Mean Absolute Error"`  
    - `"Mean Squared Error"`

**Example:**
```python
from src import evaluation

metrics = evaluation.evaluate(model, clean_df)
print(metrics)
```

---

### 4. `app.py` (Streamlit UI)

**Purpose:**  
Provides an interactive web interface for the workflow.

**Workflow:**
1. **Upload Data:**  
   User uploads a CSV file with at least a date and demand column.
2. **Select Product/Category:**  
   If available, user selects a product/item/category for targeted forecasting.
3. **Preprocess Data:**  
   Cleans and standardizes the data.
4. **Train Model:**  
   Trains a regression model on the filtered data.
5. **Forecast:**  
   User specifies forecast horizon; app generates and visualizes predictions.
6. **Evaluate:**  
   Displays model evaluation metrics.

**Key Features:**
- Dark, Apple-inspired UI via custom CSS.
- Interactive sidebar controls for each step.
- Plotly-based visualization of historical and forecasted demand.
- Supports forecasting for specific products or categories.

---

## Data Requirements

- **Date column:**  
  Accepts `date`, `order_date`, `timestamp`, or `datetime` (case-insensitive).
- **Demand column:**  
  Accepts `demand`, `sales`, `quantity`, or `units_sold` (case-insensitive).
- **Optional:**  
  `product`, `item`, or `category` column for filtering.

---

## Example Data Format

| date       | product   | demand |
|------------|-----------|--------|
| 2024-01-01 | Widget A  | 120    |
| 2024-01-02 | Widget A  | 130    |
| 2024-01-01 | Widget B  | 80     |

---

## Extending the System

- **Model:**  
  Swap out the linear regression model for more advanced time series models (Prophet, ARIMA, LSTM, etc.) in `forecasting_model.py`.
- **Preprocessing:**  
  Add feature engineering, outlier removal, or aggregation as needed.
- **UI:**  
  Add more controls, visualizations, or export options in `app.py`.

---

## Troubleshooting

- **Missing Columns:**  
  Ensure your CSV has the required columns. The app will raise clear errors if not.
- **Model Not Training:**  
  Check that preprocessing succeeded and the filtered data is not empty.
- **Forecast Looks Flat:**  
  Linear regression is simple; try a more advanced model for complex patterns.

---

## Contributing

- Fork the repo and submit pull requests for improvements.
- Please document any new features or changes.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## Contact

For questions or suggestions, please open an issue on GitHub.