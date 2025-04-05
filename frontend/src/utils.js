// utils.js

// Format currency (e.g., ₹123,456.78)
export function formatCurrency(value) {
  return new Intl.NumberFormat("en-IN", {
    style: "currency",
    currency: "INR",
    minimumFractionDigits: 2,
  }).format(value);
}

// Format percentage (e.g., 1.23%)
export function formatPercentage(value) {
  return `${value.toFixed(2)}%`;
}

// Get time in HH:MM:SS
export function getCurrentTime() {
  const now = new Date();
  return now.toLocaleTimeString("en-IN", { hour12: false });
}

// Check if WebSocket is open
export function isWebSocketOpen(ws) {
  return ws && ws.readyState === WebSocket.OPEN;
}

// Delay utility
export function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}
