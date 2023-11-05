import React, { useState } from 'react';

function App() {
  const [stockSymbol, setStockSymbol] = useState('');
  const [startDate, setStartDate] = useState('');
  const [endDate, setEndDate] = useState('');
  const [stockData, setStockData] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    // Make an API request to the backend here
    try {
      const response = await fetch('/get_stock_data', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ stock_symbol: stockSymbol, start_date: startDate, end_date: endDate }),
      });
      const data = await response.json();
      setStockData(data);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div className="App">
      <h1>Stock Price Analysis</h1>
      <form onSubmit={handleSubmit}>
        <label>
          Stock Symbol:
          <input type="text" value={stockSymbol} onChange={(e) => setStockSymbol(e.target.value)} required />
        </label>
        <br />
        <label>
          Start Date:
          <input type="date" value={startDate} onChange={(e) => setStartDate(e.target.value)} required />
        </label>
        <br />
        <label>
          End Date:
          <input type="date" value={endDate} onChange={(e) => setEndDate(e.target.value)} required />
        </label>
        <br />
        <button type="submit">Analyze</button>
      </form>
      {stockData && (
        <div>
          <h2>Stock Data:</h2>
          <pre>{JSON.stringify(stockData, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}

export default App;
