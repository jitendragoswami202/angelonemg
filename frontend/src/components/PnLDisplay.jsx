import React, { useEffect, useState } from 'react';
import axios from 'axios';

const PnLDisplay = () => {
  const [pnl, setPnl] = useState(0);

  useEffect(() => {
    axios.get('/api/pnl').then((res) => setPnl(res.data.total));
  }, []);

  return (
    <div>
      <h4>Total PnL</h4>
      <p style={{ color: pnl >= 0 ? 'green' : 'red' }}>
        {pnl.toFixed(2)}
      </p>
    </div>
  );
};

export default PnLDisplay;