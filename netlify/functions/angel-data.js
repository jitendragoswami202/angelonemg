const axios = require("axios");

exports.handler = async function (event, context) {
  const API_KEY = process.env.ANGEL_API_KEY;
  const CLIENT_CODE = process.env.ANGEL_CLIENT_CODE;
  const ACCESS_TOKEN = process.env.ANGEL_ACCESS_TOKEN;

  const headers = {
    'X-UserType': 'USER',
    'X-SourceID': 'WEB',
    'X-ClientLocalIP': '127.0.0.1',
    'X-ClientPublicIP': '127.0.0.1',
    'X-MACAddress': '00:00:00:00:00:00',
    'X-PrivateKey': API_KEY,
    'X-ClientCode': CLIENT_CODE,
    'Authorization': `Bearer ${ACCESS_TOKEN}`,
  };

  try {
    const response = await axios.post(
      "https://apiconnect.angelbroking.com/rest/secure/angelbroking/order/v1/getOrderBook",
      {}, // or your request body
      { headers }
    );

    return {
      statusCode: 200,
      body: JSON.stringify(response.data),
    };
  } catch (err) {
    return {
      statusCode: 500,
      body: JSON.stringify({ error: err.message }),
    };
  }
};