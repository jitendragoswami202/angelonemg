import React, { useEffect, useState } from "react";
import "./style.css";

const OpenOrders = () => {
  const [openOrders, setOpenOrders] = useState([]);
  const [loading, setLoading] = useState(true);

  // Simulated API call to fetch open orders
  useEffect(() => {
    const fetchOpenOrders = async () => {
      setLoading(true);

      // Mock data (replace with backend API call if available)
      const orders = [
        { id: 1, symbol: "AAPL", type: "Buy", quantity: 10, price: 173.45 },
        { id: 2, symbol: "GOOGL", type: "Sell", quantity: 5, price: 2900.12 },
        { id: 3, symbol: "TSLA", type: "Buy", quantity: 7, price: 750.25 },
      ];

      setTimeout(() => {
        setOpenOrders(orders);
        setLoading(false);
      }, 1000); // Simulate network delay
    };

    fetchOpenOrders();
  }, []);

  return (
    <div className="open-orders">
      <h2>Open Orders</h2>
      {loading ? (
        <p>Loading open orders...</p>
      ) : openOrders.length === 0 ? (
        <p>No open orders at the moment.</p>
      ) : (
        <table className="orders-table">
          <thead>
            <tr>
              <th>Order ID</th>
              <th>Symbol</th>
              <th>Type</th>
              <th>Quantity</th>
              <th>Price (USD)</th>
            </tr>
          </thead>
          <tbody>
            {openOrders.map((order) => (
              <tr key={order.id}>
                <td>{order.id}</td>
                <td>{order.symbol}</td>
                <td>{order.type}</td>
                <td>{order.quantity}</td>
                <td>{order.price.toFixed(2)}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
};

export default OpenOrders;