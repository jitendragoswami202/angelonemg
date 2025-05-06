import React, { useEffect, useState } from 'react';
import axios from 'axios';

const OpenOrders = () => {
  const [orders, setOrders] = useState([]);

  useEffect(() => {
    axios.get('/api/orders/open').then((res) => setOrders(res.data));
  }, []);

  return (
    <div>
      <h4>Open Orders</h4>
      <ul>
        {orders.map((order) => (
          <li key={order.id}>{order.symbol} - {order.side} - {order.qty} @ {order.price}</li>
        ))}
      </ul>
    </div>
  );
};

export default OpenOrders;