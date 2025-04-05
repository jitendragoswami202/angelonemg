// frontend/src/components/PnLDisplay.jsx
import React, { useContext } from 'react';
import { Paper, Typography, Grid } from '@mui/material';
import { AppContext } from '../context';

function PnLDisplay() {
    const { pnl } = useContext(AppContext);

    if (!pnl) {
        return (
            <Paper elevation={3} style={{ padding: '20px' }}>
                <Typography>Loading PnL Data...</Typography>
            </Paper>
        );
    }

    // Determine color based on PnL value
    const pnlColor = pnl >= 0 ? 'green' : 'red';

    return (
        <Paper elevation={3} style={{ padding: '20px' }}>
            <Typography variant="h6">Profit & Loss (PnL)</Typography>
            <Grid container spacing={2} style={{ marginTop: '10px' }}>
                <Grid item xs={12} sm={6}>
                    <Typography variant="subtitle1">
                        Total PnL: <span style={{ color: pnlColor }}>${pnl.toFixed(2)}</span>
                    </Typography>
                </Grid>
                {/* Add other PnL related data if needed */}
            </Grid>
        </Paper>
    );
}

export default PnLDisplay;
