import React, { useState } from 'react';
import './App.css';
import StockPlot from './stock';

function App() {
  const [stockSymbol, setStockSymbol] = useState('');
  const [startDate, setStartDate] = useState('');
  const [endDate, setEndDate] = useState('');
  const [showPlot, setShowPlot] = useState(false);

  const handleShowPlot = () => {
    setShowPlot(true);
  };

  return (
    <div className="App">
      <h1>Stock Plotter</h1>
      <div>
        <label htmlFor="stockSymbol">Stock Symbol:</label>
        <input
          id="stockSymbol"
          type="text"
          value={stockSymbol}
          onChange={(e) => setStockSymbol(e.target.value)}
        />
      </div>
      <div>
        <label htmlFor="startDate">Start Date:</label>
        <input
          id="startDate"
          type="date"
          value={startDate}
          onChange={(e) => setStartDate(e.target.value)}
        />
      </div>
      <div>
        <label htmlFor="endDate">End Date:</label>
        <input
          id="endDate"
          type="date"
          value={endDate}
          onChange={(e) => setEndDate(e.target.value)}
        />
      </div>
      <button onClick={handleShowPlot}>
        Show Plot
      </button>
      {showPlot && (
        <StockPlot
          stockSymbol={stockSymbol}
          startDate={startDate}
          endDate={endDate}
        />
      )}
    </div>
  );
}

export default App;
