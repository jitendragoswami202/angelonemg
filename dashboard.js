import React, { useEffect, useState } from 'react';
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { io } from 'socket.io-client';

const Dashboard = () => {
    const [marketData, setMarketData] = useState([]);
    const [connected, setConnected] = useState(false);

    useEffect(() => {
        const socket = io('http://localhost:5000');

        socket.on('connect', () => {
            setConnected(true);
            console.log('Connected to WebSocket server');
        });

        socket.on('disconnect', () => {
            setConnected(false);
            console.log('Disconnected from WebSocket server');
        });

        socket.on('market_data', (data) => {
            setMarketData(data);
        });

        return () => {
            socket.disconnect();
        };
    }, []);

    return (
        <div className="p-6 space-y-6">
            <Card className="bg-gray-900 text-white">
                <CardContent>
                    <h1 className="text-2xl font-bold">Trading Dashboard</h1>
                    <p>Status: {connected ? 'Connected' : 'Disconnected'}</p>
                </CardContent>
            </Card>

            <div className="grid grid-cols-2 gap-4">
                {marketData.map((item, index) => (
                    <Card key={index} className="bg-gray-800 text-white p-4">
                        <CardContent>
                            <p>{item.symbol}: {item.price}</p>
                        </CardContent>
                    </Card>
                ))}
            </div>

            <Button className="bg-blue-500 hover:bg-blue-600 text-white">Start Bot</Button>
            <Button className="bg-red-500 hover:bg-red-600 text-white">Stop Bot</Button>
        </div>
    );
};

export default Dashboard;
