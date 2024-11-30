ARIMA Model for Electricity Production Forecasting
This project utilizes an ARIMA (AutoRegressive Integrated Moving Average) model to forecast electricity production based on historical data. The dataset used in this project is from Electric_Production.csv, containing monthly electricity production values.

Model Overview:
The ARIMA model is used to capture and forecast the time-series data of electricity production.
The stationarity of the data is checked using the Augmented Dickey-Fuller (ADF) test.
Differencing is applied to make the series stationary, followed by the fitting of the ARIMA model.
The model parameters (p, d, q) are selected based on ACF and PACF plots.
A forecast for the next 24 months is generated and compared to the actual values in the test set.
Key Features:
Stationarity Testing: Augmented Dickey-Fuller (ADF) test to check for unit roots.
Differencing: To make the data stationary, if needed.
Forecasting: Predicts the future electricity production for the next 24 months.
Performance Metrics: Evaluates the model's accuracy using metrics such as MSE, RMSE, and MAE.
Tools & Libraries:
Pandas: For data manipulation.
Matplotlib: For data visualization.
Statsmodels: For ARIMA model and statistical tests.
Scikit-learn: For calculating performance metrics like MSE, RMSE, and MAE.
