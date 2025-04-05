import React, { useState, useEffect } from 'react';
import { FaWallet, FaSignOutAlt, FaRobot, FaMoon, FaSun, FaCog } from 'react-icons/fa';

const TradingDashboard = () => {
  const [botRunning, setBotRunning] = useState(false);
  const [darkMode, setDarkMode] = useState(false);
  const [profit, setProfit] = useState(0);
  const [availableFunds, setAvailableFunds] = useState(100000);
  const [totalPnL, setTotalPnL] = useState(0);
  const [notifications, setNotifications] = useState([]);
  const [currentTime, setCurrentTime] = useState(new Date().toLocaleTimeString());
  const [openPositions, setOpenPositions] = useState([]);
  const [openOrders, setOpenOrders] = useState([]);

  // WebSocket connection state
  const [ws, setWs] = useState(null);

  // Use environment variables
  const clientCode = process.env.REACT_APP_CLIENT_CODE;  // From .env
  const feedToken = process.env.REACT_APP_FEED_TOKEN;    // From .env
  const apiKey = process.env.REACT_APP_API_KEY;          // From .env

  // Initialize WebSocket connection
  useEffect(() => {
    const socketUrl = `wss://smartapisocket.angelone.in/smart-stream?clientCode=${clientCode}&feedToken=${feedToken}&apiKey=${apiKey}`;
    const socket = new WebSocket(socketUrl);

    socket.onopen = () => {
      console.log('WebSocket connection established');
      socket.send(JSON.stringify({
        action: 'subscribe',
        channels: ['market-data', 'order-status', 'account-info'],
      }));
    };

    socket.onmessage = (event) => {
      const data = JSON.parse(event.data);
      if (data.type === 'market-data') {
        // Handle market data here
      }

      if (data.type === 'order-status') {
        setOpenOrders(prev => [...prev, data.order]);
      }

      if (data.type === 'account-info') {
        setAvailableFunds(data.balance);
      }
    };

    socket.onclose = () => {
      console.log('WebSocket connection closed');
    };

    setWs(socket);

    return () => {
      if (ws) {
        ws.close();
      }
    };
  }, []);

  const toggleBot = () => {
    const message = botRunning ? 'Bot Stopped' : 'Bot Started';
    setBotRunning(!botRunning);
    setNotifications(prev => [...prev, `${message} - ${new Date().toLocaleTimeString()}`]);
  };

  const exitPosition = () => {
    const message = 'Position Exited';
    setNotifications(prev => [...prev, `${message} - ${new Date().toLocaleTimeString()}`]);
  };

  useEffect(() => {
    const timer = setInterval(() => {
      setCurrentTime(new Date().toLocaleTimeString());
    }, 1000);
    return () => clearInterval(timer);
  }, []);

  return (
    <div className={`${darkMode ? 'bg-black text-white' : 'bg-white text-black'} p-10 min-h-screen font-sans`}>
      {/* Dashboard UI components */}
    </div>
  );
};

export default TradingDashboard;
                              
