// frontend/src/services/api.js
const API_URL = 'http://your-backend-server-url/api'; // Replace with your backend API URL

export const sendBotCommand = async (command) => {
    const response = await fetch(`${API_URL}/command`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ command }),
    });
    if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
    }
    return response.json();
};
