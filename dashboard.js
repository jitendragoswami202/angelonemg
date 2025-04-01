// Dashboard.js (Dashboard Component)

import React, { useState, useEffect } from 'react';

const Dashboard = ({ accessToken }) => {
  const [accountData, setAccountData] = useState(null);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchAccountData = async () => {
      try {
        const response = await fetch('https://your-backend-server.com/account-data', {
          method: 'GET',
          headers: {
            'Authorization': `Bearer ${accessToken}`,
          },
        });

        const data = await response.json();
        setAccountData(data);
      } catch (err) {
        setError('Failed to fetch account data');
        console.error(err);
      }
    };

    if (accessToken) {
      fetchAccountData();
    }
  }, [accessToken]);

  return (
    <div>
      <h1>Account Data</h1>
      {error && <p>{error}</p>}
      {accountData ? (
        <pre>{JSON.stringify(accountData, null, 2)}</pre>
      ) : (
        <p>Loading account data...</p>
      )}
    </div>
  );
};

export default Dashboard;
