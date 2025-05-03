import React from "react";
import BotControl from "./BotControl";
import Dashboard from "./Dashboard";
import FundsInfo from "./FundsInfo";
import PnLDisplay from "./PnLDisplay";
import Positions from "./Positions";
import TradeHistory from "./TradeHistory";
import "./style.css";

const App = () => {
  return (
    <div className="app">
      <header className="header">
        <h1>Algo Trading Dashboard</h1>
      </header>
      <main className="main">
        <div className="sidebar">
          <FundsInfo />
          <PnLDisplay />
        </div>
        <div className="content">
          <Dashboard />
          <Positions />
          <TradeHistory />
        </div>
      </main>
      <footer className="footer">
        <BotControl />
      </footer>
    </div>
  );
};

export default App;