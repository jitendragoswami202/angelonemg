import React, { useEffect, useState } from 'react';
import axios from 'axios';

const Positions = () => {
  const [positions, setPositions] = useState([]);

  useEffect(() => {
    axios.get('/api/positions').then((res) => setPositions(res.data));
  }, []);

  return (
    <div>
      <h4>Open Positions</h4>
      <ul>
        {positions.map((pos) => (
          <li key={pos.symbol}>{pos.symbol}: {pos.qty} @ {pos.avgPrice}</li>
        ))}
      </ul>
    </div>
  );
};

export default Positions;