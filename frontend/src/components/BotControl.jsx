// frontend/src/components/BotControl.jsx
import React, { useState, useContext } from 'react';
import { Button, TextField, Paper, Typography } from '@mui/material';
import { AppContext } from '../context';
import { sendBotCommand } from '../services/api';

function BotControl() {
    const [command, setCommand] = useState('');
    const { setBotStatus } = useContext(AppContext);

    const handleSendCommand = async () => {
        try {
            const response = await sendBotCommand(command);
            setBotStatus(response.status);
            setCommand('');
        } catch (error) {
            console.error('Error sending command:', error);
        }
    };

    return (
        <Paper elevation={3} style={{ padding: '20px' }}>
            <Typography variant="h6">Bot Control</Typography>
            <TextField
                label="Command"
                value={command}
                onChange={(e) => setCommand(e.target.value)}
                fullWidth
                margin="normal"
            />
            <Button variant="contained" color="primary" onClick={handleSendCommand}>
                Send Command
            </Button>
        </Paper>
    );
}

export default BotControl;
