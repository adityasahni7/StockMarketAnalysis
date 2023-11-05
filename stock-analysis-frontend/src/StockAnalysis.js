import React, { useState } from 'react';
import axios from 'axios';

function StockAnalysis() {
  const [stockSymbol, setStockSymbol] = useState('');
  const [start_date, setStartDate] = useState('');
  const [end_date, setEndDate] = useState('');
  const [stockData, setStockData] = useState(null);

  const analyzeStock = () => {
    if (!stockSymbol || !start_date || !end_date) {
      alert("Please fill in all fields.");
      return;
    }

    // Fetch stock data when the "Analyze" button is clicked
    axios.get(`http://127.0.0.1:5000/stock-analysis?stock_symbol=${stockSymbol}&start_date=${start_date}&end_date=${end_date}`)
      .then((response) => {
        setStockData(response.data);
      })
      .catch((error) => {
        console.error('Error fetching data:', error);
      });
  };

  return (
    <div>
      <h1>Stock Analysis</h1>
      <div>
        <label>Stock Symbol:</label>
        <input type="text" value={stockSymbol} onChange={(e) => setStockSymbol(e.target.value)} />
      </div>
      <div>
        <label>Start Date:</label>
        <input type="date" value={start_date} onChange={(e) => setStartDate(e.target.value)} />
      </div>
      <div>
        <label>End Date:</label>
        <input type="date" value={end_date} onChange={(e) => setEndDate(e.target.value)} />
      </div>

      <button onClick={analyzeStock}>Analyze</button>

    {stockData && (
        <div>
            <h2>Stock Data:</h2>
            <pre>{JSON.stringify(stockData, null, 2)}</pre>
        </div>
    )}
    </div>
  );
}

export default StockAnalysis;
