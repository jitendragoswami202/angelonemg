import React, { useEffect, useState } from "react";
import "./style.css";

const MarketDataWidget = () => {
  const [marketData, setMarketData] = useState([]);
  const [loading, setLoading] = useState(true);

  // Simulate API call to fetch market data
  useEffect(() => {
    const fetchMarketData = async () => {
      setLoading(true);
      // Mock API data (replace with actual API call if available)
      const data = [
        { symbol: "AAPL", price: 173.45, change: "+1.23%" },
        { symbol: "GOOGL", price: 2899.12, change: "-0.45%" },
        { symbol: "AMZN", price: 3450.67, change: "+0.89%" },
        { symbol: "TSLA", price: 750.25, change: "-1.12%" },
      ];
      setTimeout(() => {
        setMarketData(data);
        setLoading(false);
      }, 1000); // Simulate network delay
    };

    fetchMarketData();
  }, []);

  return (
    <div className="market-widget">
      <h2>Market Data</h2>
      {loading ? (
        <p>Loading market data...</p>
      ) : (
        <table className="market-table">
          <thead>
            <tr>
              <th>Symbol</th>
              <th>Price (USD)</th>
              <th>Change</th>
            </tr>
          </thead>
          <tbody>
            {marketData.map((data, index) => (
              <tr key={index}>
                <td>{data.symbol}</td>
                <td>{data.price.toFixed(2)}</td>
                <td
                  className={
                    data.change.includes("+") ? "positive" : "negative"
                  }
                >
                  {data.change}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
};

export default MarketDataWidget;