// src/websocket.js
let socket;

export const connectWebSocket = (onMessage) => {
  socket = new WebSocket("wss://api.angelbroking.com/WebSocket");

  socket.onopen = () => {
    console.log("WebSocket connected");

    // Replace with your actual Angel One WebSocket subscription
    const payload = {
      correlationID: "sub-001",
      action: 1,
      params: {
        mode: 1,
        tokenList: [
          { exchangeType: 1, tokens: ["99926000"] } // Example NIFTY index token
        ]
      }
    };
    socket.send(JSON.stringify(payload));
  };

  socket.onmessage = (msg) => {
    const data = JSON.parse(msg.data);
    if (onMessage) onMessage(data);
  };

  socket.onerror = (err) => {
    console.error("WebSocket Error:", err);
  };

  socket.onclose = () => {
    console.log("WebSocket disconnected");
  };
};

export const disconnectWebSocket = () => {
  if (socket) socket.close();
};