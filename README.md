# E-Commerce Demand Forecasting System

This project is designed to forecast demand for e-commerce products using historical sales data. It includes data preprocessing, model training, and evaluation components to ensure accurate predictions.

## Project Structure

```
ecommerce-demand-forecasting
├── data
│   ├── #Upload data for prediction
├── src
│   ├── data_preprocessing.py      # Data loading and preprocessing functions
│   ├── forecasting_model.py       # Model training and forecasting functions
│   ├── evaluation.py              # Model evaluation metrics
├── app.py                         # Streamlit UI application
├── requirements.txt               # Python dependencies
├── README.md                      # Project overview and setup
├── DOCUMENTATION.md               # (This file) Detailed codebase documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone https://github.com/raza-abidii/E-Commerce-Demand-Forecasting-System
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Prepare your data:
   - Place your raw data files in the `data` directory.
   - Run the data preprocessing script to clean and transform the data.

## Usage Examples

- To preprocess the data, run:
  ```
  python src/data_preprocessing.py
  ```

- To train the forecasting model, execute:
  ```
  python src/forecasting_model.py
  ```

- To evaluate the model's performance, use:
  ```
  python src/evaluation.py
  ```
  
# UML Diagrams
### Class diagram
```mermaid
classDiagram
    class ForecastingModel {
        - model
        + __init__(model)
        + train_model(X_train, y_train)
        + predict(X_test)
        + save_model(file_path)
        + evaluate_model(X_test, y_true)
        + load_model(file_path)
    }

    class data_preprocessing {
        + load_data(file_path)
        + transform_data(data)
        + preprocess(df)
    }

    class forecasting_model {
        + train(df)
        + forecast(model, df, periods)
    }

    class evaluation {
        + calculate_metrics(y_true, y_pred)
        + plot_results(y_true, y_pred)
        + evaluate(model, df)
    }

    class app {
        + Streamlit UI
    }

    forecasting_model ..|> ForecastingModel
    app --> data_preprocessing : uses
    app --> forecasting_model : uses
    app --> evaluation : uses
```
### Object diagram
```mermaid
erDiagram
    APP ||--o{ DataFrame : uses
    APP ||--o{ ForecastingModel : uses
    APP ||--o{ Evaluation : uses
    ForecastingModel ||--o{ LinearRegression : wraps
    DataFrame {
        string date
        number demand
        string product
    }
```
### Sequence diagram
```mermaid
sequenceDiagram
    participant User
    participant App
    participant DataPreprocessing
    participant ForecastingModel
    participant Evaluation

    User->>App: Upload CSV
    App->>DataPreprocessing: preprocess(df)
    DataPreprocessing-->>App: cleaned_df
    User->>App: Select product/category
    User->>App: Click Train Model
    App->>ForecastingModel: train(cleaned_df)
    ForecastingModel-->>App: model
    User->>App: Set forecast period
    User->>App: Click Generate Forecast
    App->>ForecastingModel: forecast(model, cleaned_df, periods)
    ForecastingModel-->>App: forecast_df
    App->>Evaluation: evaluate(model, cleaned_df)
    Evaluation-->>App: metrics
    App->>User: Show chart & metrics
```
### Use Case diagram
```mermaid
flowchart TD
    User((User))
    Upload([Upload Data])
    Select([Select Product/Category])
    Preprocess([Preprocess Data])
    Train([Train Model])
    Forecast([Forecast Demand])
    View([View Results])

    User --> Upload
    User --> Select
    User --> Preprocess
    User --> Train
    User --> Forecast
    User --> View

    Upload --> Preprocess
    Preprocess --> Train
    Train --> Forecast
    Forecast --> View
```
### Collaborative diagram
```mermaid
graph TD
    User-->|uploads data|App
    App-->|calls|data_preprocessing
    App-->|calls|forecasting_model
    App-->|calls|evaluation
    data_preprocessing-->|returns cleaned data|App
    forecasting_model-->|returns model/forecast|App
    evaluation-->|returns metrics|App
    App-->|shows results|User
```
### Activity diagram
```mermaid
flowchart TD
    Start([Start])
    Upload[Upload CSV]
    Preprocess[Preprocess Data]
    Select[Select Product/Category]
    Train[Train Model]
    Forecast[Forecast Demand]
    Visualize[Visualize Results]
    End([End])

    Start --> Upload
    Upload --> Preprocess
    Preprocess --> Select
    Select --> Train
    Train --> Forecast
    Forecast --> Visualize
    Visualize --> End
```



## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
