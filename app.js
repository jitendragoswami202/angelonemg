// App.js (Main Dashboard)

import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Route, Switch, Link } from 'react-router-dom';
import Dashboard from './Dashboard';
import Login from './Login';

const App = () => {
  const [accessToken, setAccessToken] = useState(null);

  useEffect(() => {
    // Check if the access token is already in localStorage
    const token = localStorage.getItem('access_token');
    if (token) {
      setAccessToken(token);
    }
  }, []);

  return (
    <Router>
      <div>
        <nav>
          <Link to="/">Home</Link>
          <Link to="/dashboard">Dashboard</Link>
        </nav>

        <Switch>
          <Route path="/dashboard">
            {accessToken ? (
              <Dashboard accessToken={accessToken} />
            ) : (
              <Login />
            )}
          </Route>
          <Route path="/" exact>
            <h1>Welcome to the Trading Dashboard</h1>
          </Route>
        </Switch>
      </div>
    </Router>
  );
};

export default App;
