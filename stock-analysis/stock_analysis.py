import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np

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

# Add Linear Regression Model
stock_data.dropna(inplace=True)  # Drop NaN values for the regression model

# Convert datetime to ordinal
X = stock_data.index.to_series().apply(lambda x: x.toordinal()).values.reshape(-1, 1)
y = stock_data['Adj Close']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and fit the regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
predictions = model.predict(X_test)

# Plot the regression line
plt.figure(figsize=(12, 6))
plt.scatter(X_test, y_test, color='blue', label='Actual Prices')
plt.plot(X_test, predictions, color='red', linewidth=2, label='Regression Line')
plt.title(f'{stock_symbol} Linear Regression Model')
plt.xlabel('Date')
plt.ylabel('Adj Close Price')
plt.legend()
plt.show()

# Calculate and print the mean squared error
mse = mean_squared_error(y_test, predictions)
print(f'Mean Squared Error: {mse}')

# Generate future dates for prediction
future_dates = pd.date_range(end=end_date, periods=30)  # Adjust the number of periods as needed

# Convert future dates to ordinal
future_dates_ordinal = future_dates.to_series().apply(lambda x: x.toordinal()).values.reshape(-1, 1)

# Make predictions for future dates
future_predictions = model.predict(future_dates_ordinal)

# Create a DataFrame for future predictions
future_predictions_df = pd.DataFrame({'Date': future_dates, 'Predicted Adj Close': future_predictions})
future_predictions_df.set_index('Date', inplace=True)

# Plot the historical data along with future predictions
plt.figure(figsize=(12, 6))
plt.plot(stock_data['Adj Close'], label='Historical Data', color='blue')
plt.plot(future_predictions_df['Predicted Adj Close'], label='Future Predictions', color='red', linestyle='dashed')
plt.title(f'{stock_symbol} Stock Price Prediction')
plt.xlabel('Date')
plt.ylabel('Adj Close Price')
plt.legend()
plt.show()
