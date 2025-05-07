// Clock updater
function updateClock() {
  const now = new Date();
  document.getElementById("clock").textContent = now.toLocaleTimeString();
}
setInterval(updateClock, 1000);
updateClock();

// Persistent Dark Mode Toggle
const darkModeToggle = document.getElementById("darkModeToggle");
const isLight = localStorage.getItem("theme") === "light";
document.body.classList.toggle("light-mode", isLight);
darkModeToggle.checked = !isLight;

darkModeToggle.addEventListener("change", function () {
  const light = !darkModeToggle.checked;
  document.body.classList.toggle("light-mode", light);
  localStorage.setItem("theme", light ? "light" : "dark");
  playSound('themeSwitch'); // Play sound on theme change
});

// Notification dropdown
document.getElementById("notifBtn").addEventListener("click", () => {
  const panel = document.getElementById("notifPanel");
  panel.classList.toggle("show");
  playSound('notification'); // Play sound when opening notification
});

// Algo bot toggle
document.getElementById("algoToggle").addEventListener("change", (e) => {
  const isActive = e.target.checked;
  alert(isActive ? "Algo Bot Activated" : "Algo Bot Deactivated");
  if (isActive) {
    startBot();
    playSound("on"); // Play sound when activating bot
  } else {
    stopBot();
    playSound("off"); // Play sound when deactivating bot
  }
});

// Live trading data
function getLiveData() {
  const symbols = ['BTC', 'ETH', 'XRP', 'SOL', 'ADA'];
  const trades = Array.from({ length: 2 }, () => {
    const type = Math.random() > 0.5 ? 'Buy' : 'Sell';
    const symbol = symbols[Math.floor(Math.random() * symbols.length)];
    const price = `$${(2000 + Math.random() * 60000).toFixed(2)}`;
    return { type, symbol, price };
  });

  const transactions = [
    { type: 'Deposit', amount: `$${(5000 + Math.random() * 10000).toFixed(2)}` },
    { type: 'Withdraw', amount: `$${(1000 + Math.random() * 3000).toFixed(2)}` }
  ];

  return {
    funds: (50000 + Math.random() * 10000).toFixed(2),
    pnl: (Math.random() * 5000 - 2500).toFixed(2),
    entryPrice: (60000 + Math.random() * 500).toFixed(2),
    currentPrice: (62000 + Math.random() * 500).toFixed(2),
    trades,
    transactions
  };
}

// UI update function
function updateDashboard() {
  const data = getLiveData();

  // Update funds and P&L
  document.getElementById("funds").textContent = `$${data.funds}`;
  const pnlEl = document.getElementById("pnl");
  pnlEl.textContent = (data.pnl >= 0 ? "+" : "") + data.pnl;
  pnlEl.className = data.pnl >= 0 ? "pnl-positive" : "pnl-negative";

  // Update trade prices
  document.getElementById("entryPrice").textContent = data.entryPrice;
  document.getElementById("currentPrice").textContent = data.currentPrice;

  // Update trade history
  const tradeHistoryEl = document.getElementById("tradeHistory");
  tradeHistoryEl.innerHTML = "";
  data.trades.forEach(trade => {
    const li = document.createElement("li");
    li.textContent = `${trade.type} ${trade.symbol} @ ${trade.price}`;
    tradeHistoryEl.appendChild(li);
  });

  // Update transaction history
  const transactionHistoryEl = document.getElementById("transactionHistory");
  transactionHistoryEl.innerHTML = "";
  data.transactions.forEach(tx => {
    const li = document.createElement("li");
    li.textContent = `${tx.type} ${tx.amount}`;
    transactionHistoryEl.appendChild(li);
  });
}

// Bot simulation
let botInterval = null;

function startBot() {
  if (botInterval) return;
  updateDashboard();
  botInterval = setInterval(updateDashboard, 5000); // Update every 5 seconds
}

function stopBot() {
  clearInterval(botInterval);
  botInterval = null;
}

// Exit trade
document.getElementById("exitTradeBtn").addEventListener("click", () => {
  alert("Trade exited successfully.");
  flashBackground();
  playSound("exit"); // Play exit trade sound
});

// Optional: Audio cues
function playSound(type) {
  const audio = new Audio();
  switch (type) {
    case "on":
      audio.src = "https://cdn.pixabay.com/audio/2022/03/15/audio_4cf23c4f2e.mp3"; // Bot activated sound
      break;
    case "off":
      audio.src = "https://cdn.pixabay.com/audio/2022/03/15/audio_f2a8cf623b.mp3"; // Bot deactivated sound
      break;
    case "exit":
      audio.src = "https://cdn.pixabay.com/audio/2022/03/15/audio_37b232b3be.mp3"; // Exit trade sound
      break;
    case "notification":
      audio.src = "https://cdn.pixabay.com/audio/2022/03/15/audio_7e5e3b9498.mp3"; // Notification bell sound
      break;
    case "themeSwitch":
      audio.src = "https://cdn.pixabay.com/audio/2022/03/15/audio_02e1ac0012.mp3"; // Theme switch sound
      break;
  }
  audio.volume = 0.5;
  audio.play();
}

// Optional: Flash effect for trade exit
function flashBackground() {
  const widget = document.querySelector(".widget");
  widget.style.transition = "background-color 0.3s ease";
  widget.style.backgroundColor = "#444";
  setTimeout(() => {
    widget.style.backgroundColor = "var(--card-bg)";
  }, 400);
}