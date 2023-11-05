import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Define the stock symbol and date range
stock_symbol = 'AAPL'  # Change to the symbol of the stock you want to analyze
start_date = '2022-01-01'
end_date = '2023-01-01'

# Download the historical stock price data
stock_data = yf.download(stock_symbol, start=start_date, end=end_date)

# Print the first few rows of the data
print(stock_data.head())

# Basic statistics
print("Basic Statistics:")
print(stock_data['Adj Close'].describe())

# Calculate daily returns
stock_data['Daily Return'] = stock_data['Adj Close'].pct_change()

# Plot the adjusted closing price
stock_data['Adj Close'].plot(figsize=(12, 6))
plt.title(f'{stock_symbol} Adjusted Closing Price')
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()

# Plot the daily returns
stock_data['Daily Return'].plot(figsize=(12, 6), color='orange')
plt.title(f'{stock_symbol} Daily Returns')
plt.xlabel('Date')
plt.ylabel('Daily Return')
plt.show()
