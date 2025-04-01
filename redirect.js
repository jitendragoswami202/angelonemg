// redirect.js (Callback Handler)

import React, { useEffect, useState } from 'react';

const Redirect = () => {
  const [message, setMessage] = useState('');

  useEffect(() => {
    // Get the URL parameters from the query string
    const queryParams = new URLSearchParams(window.location.search);
    const authCode = queryParams.get('code');

    if (authCode) {
      // Send authorization code to backend to exchange for tokens
      fetchTokens(authCode);
    } else {
      setMessage('Authorization code not found.');
    }
  }, []);

  // Function to fetch tokens from your backend
  const fetchTokens = async (authCode) => {
    try {
      const response = await fetch('https://your-backend-server.com/exchange-token', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ code: authCode }),
      });
      const data = await response.json();
      if (data.success) {
        setMessage('Tokens obtained successfully!');
        // Optionally store the tokens in localStorage/sessionStorage or redirect the user
        localStorage.setItem('access_token', data.access_token);
        localStorage.setItem('refresh_token', data.refresh_token);
      } else {
        setMessage('Failed to exchange code for tokens.');
      }
    } catch (error) {
      console.error('Error fetching tokens:', error);
      setMessage('Error during token exchange.');
    }
  };

  return (
    <div>
      <h1>Redirecting...</h1>
      <p>{message}</p>
    </div>
  );
};

export default Redirect;
