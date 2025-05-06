import React from 'react';
import Dashboard from './components/Dashboard';
import { useAppContext } from './context';

const App = () => {
  const { theme } = useAppContext();

  return (
    <div style={{
      backgroundColor: theme.background,
      color: theme.color,
      minHeight: '100vh',
      padding: '1rem'
    }}>
      <Dashboard />
    </div>
  );
};

export default App;