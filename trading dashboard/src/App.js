import React, { useEffect, useState } from 'react';

function App() {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetch('https://your-backend-api.com/trade')  // Replace with your actual API
      .then((res) => res.json())
      .then((json) => setData(json))
      .catch((err) => console.error('Error fetching data:', err));
  }, []);

  return (
    <div style={{ padding: '20px' }}>
      <h2>Algo Trading Bot Status</h2>
      {data ? (
        <div>
          <p>Symbol: {data.symbol}</p>
          <p>Price: {data.price}</p>
          <p>Action: {data.action}</p>
        </div>
      ) : (
        <p>Loading data...</p>
      )}
    </div>
  );
}

export default App;