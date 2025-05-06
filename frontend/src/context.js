import React, { createContext, useContext, useState } from 'react';
import { themes } from './theme';

const AppContext = createContext();

export const AppProvider = ({ children }) => {
  const [symbol, setSymbol] = useState('BINANCE:BTCUSDT');
  const [botRunning, setBotRunning] = useState(false);
  const [themeName, setThemeName] = useState('dark');

  const theme = themes[themeName];

  return (
    <AppContext.Provider value={{
      symbol,
      setSymbol,
      botRunning,
      setBotRunning,
      themeName,
      setThemeName,
      theme
    }}>
      {children}
    </AppContext.Provider>
  );
};

export const useAppContext = () => useContext(AppContext);