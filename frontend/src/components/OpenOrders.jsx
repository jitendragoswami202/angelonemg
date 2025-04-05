// frontend/src/components/OpenOrder.jsx
import React, { useContext, useState } from 'react';
import { Paper, Typography, Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Button, TextField } from '@mui/material';
import { AppContext } from '../context';

function OpenOrder() {
    const { openOrders } = useContext(AppContext);
    const [symbol, setSymbol] = useState('');
    const [quantity, setQuantity] = useState('');
    const [price, setPrice] = useState('');

    const handlePlaceOrder = () => {
        // In a real application, you would send this data to your backend
        console.log('Placing order:', { symbol, quantity, price });
        // You would likely call an API here to place the order
        // and then update the openOrders state in the context
        setSymbol('');
        setQuantity('');
        setPrice('');
    };

    return (
        <Paper elevation={3} style={{ padding: '20px' }}>
            <Typography variant="h6">Open Orders</Typography>
            <TableContainer>
                <Table>
                    <TableHead>
                        <TableRow>
                            <TableCell>Symbol</TableCell>
                            <TableCell>Quantity</TableCell>
                            <TableCell>Price</TableCell>
                            <TableCell>Status</TableCell>
                        </TableRow>
                    </TableHead>
                    <TableBody>
                        {openOrders && openOrders.map((order, index) => (
                            <TableRow key={index}>
                                <TableCell>{order.symbol}</TableCell>
                                <TableCell>{order.quantity}</TableCell>
                                <TableCell>{order.price}</TableCell>
                                <TableCell>{order.status}</TableCell>
                            </TableRow>
                        ))}
                         {/* Example row, replace with dynamic data */}
                    </TableBody>
                </Table>
            </TableContainer>

            <Typography variant="h6" style={{ marginTop: '20px' }}>Place New Order</Typography>
            <Grid container spacing={2} style={{ marginTop: '10px' }}>
                <Grid item xs={12} sm={4}>
                    <TextField
                        label="Symbol"
                        value={symbol}
                        onChange={(e) => setSymbol(e.target.value)}
                        fullWidth
                    />
                </Grid>
                <Grid item xs={12} sm={4}>
                    <TextField
                        label="Quantity"
                        value={quantity}
                        onChange={(e) => setQuantity(e.target.value)}
                        fullWidth
                    />
                </Grid>
                <Grid item xs={12} sm={4}>
                    <TextField
                        label="Price"
                        value={price}
                        onChange={(e) => setPrice(e.target.value)}
                        fullWidth
                    />
                </Grid>
                <Grid item xs={12}>
                    <Button variant="contained" color="primary" onClick={handlePlaceOrder}>
                        Place Order
                    </Button>
                </Grid>
            </Grid>
        </Paper>
    );
}

export default OpenOrder;
