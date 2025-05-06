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

export default Dashboard;