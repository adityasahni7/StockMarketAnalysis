import React, { useState, useEffect } from 'react';

const StockPlot = ({ stockSymbol, startDate, endDate }) => {
  const [imageUrl, setImageUrl] = useState('');

  useEffect(() => {
    const fetchPlot = async () => {
     
      const url = `http://127.0.0.1:5000/stock/${stockSymbol}/${startDate}/${endDate}`;
      try {
      
        const response = await fetch(url);
        if (response.ok) {
          
          setImageUrl(url);
        } else {
          
          console.error('Server responded with error:', response.status);
        }
      } catch (error) {
        console.error('Fetching plot failed:', error);
      }
    };

    if (stockSymbol && startDate && endDate) {
      fetchPlot();
    }
  }, [stockSymbol, startDate, endDate]);

  return (
    <div>
      <h1>{stockSymbol} Stock Plot</h1>
      {imageUrl ? <img src={imageUrl} alt={`${stockSymbol} Stock Plot`} /> : <p>Loading plot...</p>}
    </div>
  );
};

export default StockPlot;
