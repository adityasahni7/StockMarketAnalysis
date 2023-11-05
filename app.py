import matplotlib
matplotlib.use('Agg')  
from flask import Flask, send_file, request
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/stock/*": {"origins": "*"}})

@app.route('/stock/<symbol>/<start_date>/<end_date>')
def stock_analysis(symbol, start_date, end_date):
    stock_data = yf.download(symbol, start=start_date, end=end_date)

    stock_data['Daily Return'] = stock_data['Adj Close'].pct_change()

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 12))

    stock_data['Adj Close'].plot(ax=ax1)
    ax1.set_title(f'{symbol} Adjusted Closing Price')
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Price')

    stock_data['Daily Return'].plot(ax=ax2, color='green')
    ax2.set_title(f'{symbol} Daily Returns')
    ax2.set_xlabel('Date')
    ax2.set_ylabel('Daily Return')

    plt.tight_layout()

    img = BytesIO()
    plt.savefig(img, format='png')
    plt.close(fig)
    img.seek(0) 

    return send_file(img, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)