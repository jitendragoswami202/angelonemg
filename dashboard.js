import React, { useState, useEffect } from 'react';
import styled, { createGlobalStyle } from 'styled-components';
import axios from 'axios';

// Global Styles for Dark/Light Mode
const GlobalStyle = createGlobalStyle`
  body {
    background-color: ${(props) => (props.darkMode ? '#121212' : '#f5f5f5')};
    color: ${(props) => (props.darkMode ? '#e0e0e0' : '#333')};
    font-family: Arial, sans-serif;
    transition: all 0.3s ease;
  }
`;

// Styled components for the dashboard layout
const Container = styled.div`
  display: flex;
  flex-direction: column;
  padding: 20px;
`;

const Header = styled.div`
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 24px;
  font-weight: bold;
`;

const ModeButton = styled.button`
  background-color: ${(props) => (props.darkMode ? '#444' : '#ccc')};
  color: ${(props) => (props.darkMode ? '#fff' : '#000')};
  border: none;
  padding: 10px;
  cursor: pointer;
  border-radius: 5px;
`;

const DashboardSection = styled.div`
  margin: 20px 0;
  padding: 10px;
  background-color: ${(props) => (props.darkMode ? '#333' : '#fff')};
  border-radius: 10px;
  box-shadow: ${(props) => (props.darkMode ? '0 0 10px rgba(0,0,0,0.5)' : '0 0 10px rgba(0,0,0,0.1)')};
`;

const Button = styled.button`
  padding: 10px;
  margin: 10px 0;
  background-color: ${(props) => (props.darkMode ? '#1a73e8' : '#4caf50')};
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
`;

const DataItem = styled.div`
  margin: 10px 0;
`;

const TradingDashboard = () => {
  const [darkMode, setDarkMode] = useState(true);
  const [funds, setFunds] = useState(0);
  const [pnl, setPnl] = useState(0);
  const [openPositions, setOpenPositions] = useState([]);
  const [openOrders, setOpenOrders] = useState([]);
  const [isBotRunning, setIsBotRunning] = useState(false);

  useEffect(() => {
    // Fetch funds, P&L, open positions, and open orders from the backend/API
    const fetchData = async () => {
      try {
        const fundsResponse = await axios.get('/api/funds');
        const pnlResponse = await axios.get('/api/pnl');
        const positionsResponse = await axios.get('/api/open-positions');
        const ordersResponse = await axios.get('/api/open-orders');
        
        setFunds(fundsResponse.data.funds);
        setPnl(pnlResponse.data.pnl);
        setOpenPositions(positionsResponse.data.positions);
        setOpenOrders(ordersResponse.data.orders);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, [isBotRunning]);

  const handleModeToggle = () => {
    setDarkMode((prevMode) => !prevMode);
  };

  const handleStartBot = () => {
    // Start the trading bot via API or backend integration
    setIsBotRunning(true);
  };

  const handleStopBot = () => {
    // Stop the trading bot via API or backend integration
    setIsBotRunning(false);
  };

  const handleExitPosition = (positionId) => {
    // Handle position exit logic via API or backend integration
    console.log(`Exiting position: ${positionId}`);
  };

  return (
    <>
      <GlobalStyle darkMode={darkMode} />
      <Container>
        <Header>
          <div>Trading Dashboard</div>
          <ModeButton darkMode={darkMode} onClick={handleModeToggle}>
            {darkMode ? 'Switch to Light Mode' : 'Switch to Dark Mode'}
          </ModeButton>
        </Header>
        
        <DashboardSection darkMode={darkMode}>
          <h3>Available Funds</h3>
          <DataItem>₹ {funds}</DataItem>
        </DashboardSection>
        
        <DashboardSection darkMode={darkMode}>
          <h3>Total P&L</h3>
          <DataItem>₹ {pnl}</DataItem>
        </DashboardSection>

        <DashboardSection darkMode={darkMode}>
          <h3>Open Positions</h3>
          {openPositions.length > 0 ? (
            openPositions.map((position) => (
              <div key={position.id}>
                <DataItem>
                  {position.name} | {position.quantity} | 
                  <Button darkMode={darkMode} onClick={() => handleExitPosition(position.id)}>Exit Position</Button>
                </DataItem>
              </div>
            ))
          ) : (
            <DataItem>No open positions.</DataItem>
          )}
        </DashboardSection>

        <DashboardSection darkMode={darkMode}>
          <h3>Open Orders</h3>
          {openOrders.length > 0 ? (
            openOrders.map((order) => (
              <DataItem key={order.id}>
                {order.symbol} | {order.quantity} | {order.status}
              </DataItem>
            ))
          ) : (
            <DataItem>No open orders.</DataItem>
          )}
        </DashboardSection>

        <Button darkMode={darkMode} onClick={isBotRunning ? handleStopBot : handleStartBot}>
          {isBotRunning ? 'Stop Bot' : 'Start Bot'}
        </Button>
      </Container>
    </>
  );
};

export default TradingDashboard;
