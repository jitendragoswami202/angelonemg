import React from 'react';
import MarketDataWidget from './components/MarketDataWidget';
import RealTimeData from './components/RealTimeData';

const App = () => (
  <div>
    <h1>Algo Trading Dashboard</h1>
    <MarketDataWidget symbol="BINANCE:BTCUSDT" />
    <RealTimeData />
  </div>
);

export default App;