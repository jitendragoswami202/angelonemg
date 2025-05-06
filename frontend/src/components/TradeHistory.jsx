import React, { useEffect, useState } from 'react';
import axios from 'axios';

const TradeHistory = () => {
  const [trades, setTrades] = useState([]);

  useEffect(() => {
    axios.get('/api/trades').then((res) => setTrades(res.data));
  }, []);

  return (
    <div>
      <h4>Trade History</h4>
      <ul>
        {trades.map((trade) => (
          <li key={trade.id}>
            {trade.symbol} - {trade.side} {trade.qty} @ {trade.price} [{trade.timestamp}]
          </li>
        ))}
      </ul>
    </div>
  );
};

export default TradeHistory;