import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import yfinance as yf

"""
This helper class to:
1. Download historical stock data from Yahoo Finance
2. Train a simple Linear Regression trend model
3. Forecast future stock prices
4. Visualize historical prices, trend line, and forecast

NOTE:
This model is educational only. 
A linear regression assumes the price follows a straight-line trend,
which is NOT realistic for financial markets.
"""

# Class to download stock data, build regression model,forecast future prices, and visualize results
class StockPricePredictor:
    def __init__(self, ticker, start_date, end_date):
        
        """
        Initialize predictor configuration.

        Parameters
        ticker : Stock symbol (e.g., "PYPL", "AAPL")
        start_date : Start date for historical stock price data (YYYY-MM-DD)
        end_date : End date for historical stock price data (YYYY-MM-DD)
        """

        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date
        self.data = None
        self.model = LinearRegression()
   
    def download_data(self):
        # Download historical stock price data from Yahoo Finance
        self.data = yf.download(self.ticker, start=self.start_date, end=self.end_date)
        
        # Flatten MultiIndex columns if needed (sometimes yfinance returns multi-level columns)
        if isinstance(self.data.columns, pd.MultiIndex):
            self.data.columns = [c[0] for c in self.data.columns]
        
        # Prepare dataframe
        self.data.reset_index(inplace=True)
        self.data['Date'] = pd.to_datetime(self.data['Date'])
        self.data.set_index('Date', inplace=True)
        self.data['Close'] = self.data['Close'].astype(float)

    def prepare_data(self):
        # Number of days since the first date used as feature
        self.data['Days'] = (self.data.index - self.data.index[0]).days
        
        X = self.data['Days'].values.reshape(-1, 1)
        y = self.data['Close'].values
        
        # Train model
        self.model.fit(X, y)
        
        # Add trend line based on trained model
        self.data['Trend'] = self.model.predict(X)

    def predict_future(self, days_ahead=365):
        # Predict future stock prices
        future_days = np.arange(
            self.data['Days'].max() + 1, 
            self.data['Days'].max() + days_ahead + 1
        ).reshape(-1, 1)
        
        future_prices = self.model.predict(future_days)

        # Create date range for predictions
        future_dates = pd.date_range(
            start=self.data.index[-1] + pd.Timedelta(days=1), 
            periods=days_ahead
        )
        
        predicted_prices = pd.DataFrame(
            data=future_prices, 
            index=future_dates, 
            columns=['Predicted']
        )
        
        return predicted_prices

    # Visualize historical data, trend, and forecast
    def plot_results(self, predicted_prices):
        full_data = pd.concat(
            [self.data[['Close', 'Trend']], predicted_prices], 
            axis=1
        )

        plt.figure(figsize=(14, 7))
        plt.plot(full_data.index, full_data['Close'], label='Actual Stock Price', color='blue')
        plt.plot(full_data.index, full_data['Trend'], label='Trend (Linear Regression)', color='orange')
        plt.plot(predicted_prices.index, predicted_prices['Predicted'], label='1-Year Forecast', color='red')
        plt.title(f'{self.ticker} Stock Price and 1-Year Forecast')
        plt.xlabel('Date')
        plt.ylabel('Price (USD)')
        plt.legend()
        plt.grid()
        plt.show()

if __name__ == "__main__":
    # Create predictor instance
    predictor = StockPricePredictor(
        ticker='PYPL', 
        start_date='2019-09-27', 
        end_date='2024-09-27'
    )
    
    # End-to-end execution
    predictor.download_data()
    predictor.prepare_data()
    predicted_prices = predictor.predict_future()
    predictor.plot_results(predicted_prices)