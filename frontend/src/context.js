// frontend/src/context.js
import React, { createContext, useState, useEffect } from 'react';
import { connectSocket } from './services/websocket';

export const AppContext = createContext();

export const AppProvider = ({ children }) => {
    const [marketData, setMarketData] = useState([]);
    const [positions, setPositions] = useState([]);
    const [tradeHistory, setTradeHistory] = useState([]);
    const [botStatus, setBotStatus] = useState('Stopped');

    useEffect(() => {
        const disconnect = connectSocket(setMarketData, setPositions, setTradeHistory, setBotStatus);
        return () => disconnect();
    }, []);

    const value = {
        marketData,
        positions,
        tradeHistory,
        botStatus,
        setBotStatus
    };

    return (
        <AppContext.Provider value={value}>
            {children}
        </AppContext.Provider>
    );
};
