import React, { useContext } from 'react';
import { Paper, Typography, Table, TableBody, TableCell, TableContainer, TableHead, TableRow } from '@mui/material';
import { AppContext } from '../context';

function Positions() {
    const { positions } = useContext(AppContext);

    return (
        <Paper elevation={3} style={{ padding: '20px' }}>
            <Typography variant="h6">Open Positions</Typography>
            <TableContainer>
                <Table>
                    <TableHead>
                        <TableRow>
                            <TableCell>Symbol</TableCell>
                            <TableCell>Quantity</TableCell>
                            <TableCell>Entry Price</TableCell>
                        </TableRow>
                    </TableHead>
                    <TableBody>
                        {positions.map((position, index) => (
                            <TableRow key={index}>
                                <TableCell>{position.symbol}</TableCell>
                                <TableCell>{position.quantity}</TableCell>
                                <TableCell>{position.entryPrice}</TableCell>
                            </TableRow>
                        ))}
                    </TableBody>
                </Table>
            </TableContainer>
        </Paper>
    );
}

export default Positions;
