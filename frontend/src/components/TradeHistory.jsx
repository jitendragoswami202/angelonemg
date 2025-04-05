import React, { useContext } from 'react';
import { Paper, Typography, Table, TableBody, TableCell, TableContainer, TableHead, TableRow } from '@mui/material';
import { AppContext } from '../context';

function TradeHistory() {
    const { tradeHistory } = useContext(AppContext);

    return (
        <Paper elevation={3} style={{ padding: '20px' }}>
            <Typography variant="h6">Trade History</Typography>
            <TableContainer>
                <Table>
                    <TableHead>
                        <TableRow>
                            <TableCell>Symbol</TableCell>
                            <TableCell>Quantity</TableCell>
                            <TableCell>Price</TableCell>
                            <TableCell>Timestamp</TableCell>
                        </TableRow>
                    </TableHead>
                    <TableBody>
                        {tradeHistory.map((trade, index) => (
                            <TableRow key={index}>
                                <TableCell>{trade.symbol}</TableCell>
                                <TableCell>{trade.quantity}</TableCell>
                                <TableCell>{trade.price}</TableCell>
                                <TableCell>{trade.timestamp}</TableCell>
                            </TableRow>
                        ))}
                    </TableBody>
                </Table>
            </TableContainer>
        </Paper>
    );
}

export default TradeHistory;
