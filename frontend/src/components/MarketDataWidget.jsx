import React, { useEffect, useRef } from 'react';
import { useAppContext } from '../context';

const MarketDataWidget = () => {
  const { symbol } = useAppContext();
  const containerRef = useRef(null);

  useEffect(() => {
    const script = document.createElement('script');
    script.src = 'https://s3.tradingview.com/tv.js';
    script.async = true;

    script.onload = () => {
      if (window.TradingView && containerRef.current) {
        new window.TradingView.widget({
          autosize: true,
          symbol,
          interval: '5',
          timezone: 'Etc/UTC',
          theme: 'dark',
          style: '1',
          locale: 'en',
          container_id: 'tv_chart_container'
        });
      }
    };

    document.head.appendChild(script);
  }, [symbol]);

  return <div id="tv_chart_container" ref={containerRef} style={{ height: '500px', width: '100%' }} />;
};

export default MarketDataWidget;