// frontend/src/components/FundsInfo.jsx
import React, { useContext } from 'react';
import { Paper, Typography, Grid } from '@mui/material';
import { AppContext } from '../context';

function FundsInfo() {
    const { funds } = useContext(AppContext);

    if (!funds) {
        return (
            <Paper elevation={3} style={{ padding: '20px' }}>
                <Typography>Loading Funds Information...</Typography>
            </Paper>
        );
    }

    return (
        <Paper elevation={3} style={{ padding: '20px' }}>
            <Typography variant="h6">Funds Information</Typography>
            <Grid container spacing={2} style={{ marginTop: '10px' }}>
                <Grid item xs={12} sm={6}>
                    <Typography variant="subtitle1">
                        Available Balance: ${funds.availableBalance.toFixed(2)}
                    </Typography>
                </Grid>
                <Grid item xs={12} sm={6}>
                    <Typography variant="subtitle1">
                        Total Equity: ${funds.totalEquity.toFixed(2)}
                    </Typography>
                </Grid>
                <Grid item xs={12} sm={6}>
                    <Typography variant="subtitle1">
                        Used Margin: ${funds.usedMargin.toFixed(2)}
                    </Typography>
                </Grid>
                <Grid item xs={12} sm={6}>
                    <Typography variant="subtitle1">
                        Free Margin: ${funds.freeMargin.toFixed(2)}
                    </Typography>
                </Grid>
            </Grid>
        </Paper>
    );
}

export default FundsInfo;
