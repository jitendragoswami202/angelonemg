// App.js (Main Dashboard)
import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Route, Routes, Link, Navigate } from 'react-router-dom';
import Dashboard from './Dashboard';
import Login from './Login';
import './style.css';  // Assuming you're using Tailwind CSS

const App = () => {
  const [accessToken, setAccessToken] = useState(null);

  useEffect(() => {
    const token = sessionStorage.getItem('access_token'); // Improved: Using sessionStorage
    if (token) {
      setAccessToken(token);
    }
  }, []);

  const handleLogout = () => {
    sessionStorage.removeItem('access_token');
    setAccessToken(null);
  };

  return (
    <Router>
      <div className="min-h-screen bg-gray-900 text-white">
        <nav className="p-4 bg-gray-800 shadow-lg flex justify-between items-center">
          <div>
            <Link to="/" className="text-xl font-bold text-blue-400">Trading Dashboard</Link>
          </div>
          <div>
            {accessToken ? (
              <>
                <Link to="/dashboard" className="mr-4 hover:text-blue-300">Dashboard</Link>
                <button onClick={handleLogout} className="bg-red-500 px-3 py-1 rounded-md">Logout</button>
              </>
            ) : (
              <Link to="/login" className="hover:text-blue-300">Login</Link>
            )}
          </div>
        </nav>

        <div className="p-4">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/login" element={<Login setAccessToken={setAccessToken} />} />
            <Route 
              path="/dashboard" 
              element={accessToken ? <Dashboard accessToken={accessToken} /> : <Navigate to="/login" />} 
            />
          </Routes>
        </div>
      </div>
    </Router>
  );
};

const Home = () => (
  <div className="text-center mt-8">
    <h1 className="text-4xl font-bold text-blue-400">Welcome to the Trading Dashboard</h1>
    <p className="text-gray-400 mt-4">Please login to access your dashboard.</p>
  </div>
);

export default App;
