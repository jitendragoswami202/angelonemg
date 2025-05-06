import React, { createContext, useContext, useState } from 'react';

// Create the context
const AppContext = createContext();

// Provider component
export const AppProvider = ({ children }) => {
  const [symbol, setSymbol] = useState('BINANCE:BTCUSDT');
  const [botRunning, setBotRunning] = useState(false);

  return (
    <AppContext.Provider value={{
      symbol,
      setSymbol,
      botRunning,
      setBotRunning
    }}>
      {children}
    </AppContext.Provider>
  );
};

// Hook to use the context
export const useAppContext = () => useContext(AppContext);