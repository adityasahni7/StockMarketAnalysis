import matplotlib
matplotlib.use('Agg')  
from flask import Flask, send_file, request
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/stock/<symbol>/<start_date>/<end_date>')
def stock_analysis(symbol, start_date, end_date):
    # Download the historical stock price data
    stock_data = yf.download(symbol, start=start_date, end=end_date)

    # Calculate daily returns
    stock_data['Daily Return'] = stock_data['Adj Close'].pct_change()

    # Plot the adjusted closing price and save to a BytesIO object
    plt.figure(figsize=(12, 6))
    stock_data['Adj Close'].plot()
    plt.title(f'{symbol} Adjusted Closing Price')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.tight_layout()
    img = BytesIO()
    plt.savefig(img, format='png')
    plt.close()
    img.seek(0)  # go to the beginning of the BytesIO object

    return send_file(img, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
