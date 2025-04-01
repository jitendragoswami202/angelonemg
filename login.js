// Login.js (Login Page)

import React from 'react';

const Login = () => {
  const clientId = process.env.REACT_APP_CLIENT_ID;
  const redirectUri = process.env.REACT_APP_REDIRECT_URL;
  
  const authorizeURL = `https://smartapi.angelone.in/publisher-login?client_id=${clientId}&redirect_uri=${redirectUri}&response_type=code`;

  return (
    <div>
      <h1>Login to Angel One</h1>
      <button onClick={() => window.location.href = authorizeURL}>Login with Angel One</button>
    </div>
  );
};

export default Login;
