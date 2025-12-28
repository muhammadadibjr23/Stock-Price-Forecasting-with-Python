import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import yfinance as yf

# Downloading PYPL stock price data from Yahoo Finance
ticker = 'PYPL'
data = yf.download(ticker, start='2019-09-27', end='2024-09-27')

# Flatten MultiIndex columns if needed (sometimes yfinance returns multi-level columns)
if isinstance(data.columns, pd.MultiIndex):
    data.columns = [c[0] for c in data.columns]

data.reset_index(inplace=True)

# Select the date and closing price columns
data['Date'] = pd.to_datetime(data['Date'])
data.set_index('Date', inplace=True)
data['Close'] = data['Close'].astype(float)

# Preparing data for regression
data['Days'] = (data.index - data.index[0]).days  # Menghitung hari sejak awal
X = data['Days'].values.reshape(-1, 1)  # Fitur
y = data['Close'].values  # Target

# Creating linear regression model
model = LinearRegression()

# Train model
model.fit(X, y)

# Add trend line based on trained model
data['Trend'] = model.predict(X)

# Predicting one year ahead
future_days = np.arange(data['Days'].max() + 1, data['Days'].max() + 365 + 1).reshape(-1, 1)
future_prices = model.predict(future_days)

# Creating DataFrame for prediction
future_dates = pd.date_range(start=data.index[-1] + pd.Timedelta(days=1), periods=365)
predicted_prices = pd.DataFrame(data=future_prices, index=future_dates, columns=['Predicted'])

# Combining original data with predictions
full_data = pd.concat([data[['Close', 'Trend']], predicted_prices], axis=1)

# Plotting
plt.figure(figsize=(14, 7))
plt.plot(full_data.index, full_data['Close'], label='Actual Stock Price', color='blue')
plt.plot(full_data.index, full_data['Trend'], label='Trend (Linear Regression)', color='orange')
plt.plot(predicted_prices.index, predicted_prices['Predicted'], label='1-Year Forecast', color='red')
plt.title('PayPal (PYPL) Stock Price and 1-Year Forecast')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid()
plt.show()
