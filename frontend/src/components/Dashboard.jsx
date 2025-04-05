import React, { useContext } from 'react';
import MarketDataWidget from './MarketDataWidget';
import Positions from './Positions';
import TradeHistory from './TradeHistory';
import BotControl from './BotControl';
import { AppContext } from '../context';
import { Grid } from '@mui/material';

function Dashboard() {
    const { marketData } = useContext(AppContext);

    return (
        <Grid container spacing={2}>
            <Grid item xs={12} md={6}>
                <MarketDataWidget marketData={marketData} />
            </Grid>
            <Grid item xs={12} md={6}>
                <Positions />
            </Grid>
            <Grid item xs={12} md={6}>
                <TradeHistory />
            </Grid>
            <Grid item xs={12} md={6}>
                <BotControl />
            </Grid>
        </Grid>
    );
}

export default Dashboard;
