from flask import Flask, request, jsonify
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route('/api/analyze', methods=['GET'])
def analyze_stock():
    # Get user input for the stock symbol, start date, and end date from query parameters
    stock_symbol = request.args.get('symbol')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    if not stock_symbol or not start_date or not end_date:
        return jsonify({'error': 'Please provide stock symbol, start date, and end date'})

    try:
        # Download the historical stock price data
        stock_data = yf.download(stock_symbol, start=start_date, end=end_date)

        # Calculate daily returns
        stock_data['Daily Return'] = stock_data['Adj Close'].pct_change()

        # Convert stock data to a dictionary for JSON response
        stock_data_dict = stock_data.to_dict()

        return jsonify(stock_data_dict)

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
