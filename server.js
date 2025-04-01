// server.js (Backend Server)

const express = require('express');
const fetch = require('node-fetch');
require('dotenv').config();

const app = express();
const PORT = process.env.PORT || 5000;

app.use(express.json());

// Exchange authorization code for tokens
app.post('/exchange-token', async (req, res) => {
  const { code } = req.body;

  const tokenUrl = 'https://api.angelone.in/oauth/token';
  const clientId = process.env.CLIENT_ID;
  const clientSecret = process.env.CLIENT_SECRET;
  const redirectUri = process.env.REDIRECT_URL;

  const payload = {
    client_id: clientId,
    client_secret: clientSecret,
    grant_type: 'authorization_code',
    code: code,
    redirect_uri: redirectUri,
  };

  try {
    const response = await fetch(tokenUrl, {
      method: 'POST',
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
      body: new URLSearchParams(payload),
    });

    const data = await response.json();

    if (data.access_token) {
      res.json({
        success: true,
        access_token: data.access_token,
        refresh_token: data.refresh_token,
      });
    } else {
      res.status(400).json({ success: false, message: 'Failed to obtain tokens' });
    }
  } catch (error) {
    console.error('Error exchanging code for tokens:', error);
    res.status(500).json({ success: false, message: 'Server error' });
  }
});

// Endpoint to fetch account data
app.get('/account-data', async (req, res) => {
  const accessToken = req.headers['authorization'].split(' ')[1];

  const accountDataUrl = 'https://api.angelone.in/v1/user/account';
  try {
    const response = await fetch(accountDataUrl, {
      method: 'GET',
      headers: {
        Authorization: `Bearer ${accessToken}`,
      },
    });
    const data = await response.json();
    res.json(data);
  } catch (error) {
    console.error('Error fetching account data:', error);
    res.status(500).json({ success: false, message: 'Error fetching account data' });
  }
});

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
