import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Get user input for the stock symbol
stock_symbol = input("Enter the stock symbol you want to analyze: ")

# Get user input for the start date
start_date = input("Enter the start date (YYYY-MM-DD): ")

# Get user input for the end date
end_date = input("Enter the end date (YYYY-MM-DD): ")

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
