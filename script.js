// Connect to WebSocket for live data
const ws = new WebSocket("wss://smartapisocket.angelbroking.com/ws");

ws.onmessage = function(event) {
    document.getElementById("data-feed").innerText = event.data;
};

// Function to place an order via API
function placeOrder() {
    const symbol = document.getElementById("symbol").value;
    const quantity = document.getElementById("quantity").value;
    const price = document.getElementById("price").value;

    fetch("/place_order", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ symbol, quantity, price })
    })
    .then(response => response.json())
    .then(data => alert("✅ Order Placed: " + JSON.stringify(data)))
    .catch(error => console.error("❌ Order Failed", error));
}
