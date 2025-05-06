import React, { useEffect, useState } from 'react';

function App() {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetch('https://your-backend-api.com/trade') // Replace with your API
      .then((res) => res.json())
      .then(setData)
      .catch(console.error);
  }, []);

  return (
    <div style={{ padding: '20px' }}>
      <h2>Algo Trading Bot Dashboard</h2>
      {data ? (
        <div>
          <p>Symbol: {data.symbol}</p>
          <p>Price: {data.price}</p>
          <p>Action: {data.action}</p>
        </div>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
}

export default App;