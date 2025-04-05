import { io } from 'socket.io-client';

const socket = io('http://your-backend-server-url'); // Replace with your backend URL

export const connectSocket = (setMarketData, setPositions, setTradeHistory, setBotStatus) => {
    socket.on('connect', () => {
        console.log('WebSocket connected');
    });

    socket.on('marketData', (data) => {
        setMarketData((prev) => [...prev, data]);
    });

    socket.on('positions', (data) => {
        setPositions(data);
    });

    socket.on('tradeHistory', (data) => {
        setTradeHistory((prev) => [...prev, data]);
    });

    socket.on('botStatus', (data) => {
        setBotStatus(data);
    });

    socket.on('disconnect', () => {
        console.log('WebSocket disconnected');
    });

    return () => {
        socket.disconnect();
    };
};
