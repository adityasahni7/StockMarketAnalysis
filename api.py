from flask import Flask, request, jsonify
import yfinance as yf

app = Flask(__name)

@app.route('/get_stock_data', methods=['POST'])
def get_stock_data():
    data = request.get_json()
    stock_symbol = data['stock_symbol']
    start_date = data['start_date']
    end_date = data['end_date']

    stock_data = yf.download(stock_symbol, start=start_date, end=end_date)
    return stock_data.to_json(orient='split')

if __name__ == '__main__':
    app.run()
