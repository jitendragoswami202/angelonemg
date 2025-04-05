// frontend/src/components/MarketDataWidget.jsx
import React, { useContext } from 'react';
import { Paper, Typography } from '@mui/material';
import { AppContext } from '../context';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from 'recharts';

function MarketDataWidget() {
    const { marketData } = useContext(AppContext);

    if (!marketData || marketData.length === 0) {
        return <Paper elevation={3} style={{ padding: '20px' }}><Typography>Loading Market Data...</Typography></Paper>;
    }
    return (
        <Paper elevation={3} style={{ padding: '20px' }}>
            <Typography variant="h6">Market Data</Typography>
            <LineChart width={500} height={300} data={marketData}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="timestamp" />
                <YAxis />
                <Tooltip />
                <Legend />
                <Line type="monotone" dataKey="price" stroke="#8884d8" name="Price"/>
            </LineChart>
        </Paper>
    );
}

export default MarketDataWidget;
