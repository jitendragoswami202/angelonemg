import React from 'react';
import MarketDataWidget from './MarketDataWidget';
import PnLDisplay from './PnLDisplay';
import Positions from './Positions';
import OpenOrders from './OpenOrders';
import TradeHistory from './TradeHistory';
import BotControl from './BotControl';
import FundsInfo from './FundsInfo';

const Dashboard = () => {
  return (
    <div>
      <BotControl />
      <MarketDataWidget symbol="BINANCE:BTCUSDT" />
      <FundsInfo />
      <PnLDisplay />
      <Positions />
      <OpenOrders />
      <TradeHistory />
    </div>
  );
};


import React from 'react';
import { useAppContext } from '../context';

const ThemeToggle = () => {
  const { themeName, setThemeName } = useAppContext();

  return (
    <button onClick={() => setThemeName(themeName === 'light' ? 'dark' : 'light')}>
      Switch to {themeName === 'light' ? 'Dark' : 'Light'} Mode
    </button>
  );
};

export default ThemeToggle;

export default Dashboard;