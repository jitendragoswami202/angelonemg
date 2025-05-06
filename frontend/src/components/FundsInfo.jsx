import React, { useEffect, useState } from 'react';
import axios from 'axios';

const FundsInfo = () => {
  const [funds, setFunds] = useState(null);

  useEffect(() => {
    axios.get('/api/funds').then((res) => setFunds(res.data));
  }, []);

  return (
    <div>
      <h4>Funds Info</h4>
      {funds ? (
        <ul>
          {Object.entries(funds).map(([currency, balance]) => (
            <li key={currency}>{currency}: {balance}</li>
          ))}
        </ul>
      ) : 'Loading...'}
    </div>
  );
};

export default FundsInfo;