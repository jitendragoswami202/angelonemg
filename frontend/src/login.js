import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";

const Login = () => {
    const [apiKey, setApiKey] = useState('');
    const [apiSecret, setApiSecret] = useState('');
    const navigate = useNavigate();

    const handleSubmit = async (e) => {
        e.preventDefault();

        const response = await fetch('/api/authenticate', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ apiKey, apiSecret })
        });

        const data = await response.json();

        if (data.success) {
            navigate('/dashboard');
        } else {
            alert('Authentication failed. Please check your API credentials.');
        }
    };

    return (
        <div className="flex justify-center items-center h-screen bg-gray-900">
            <Card className="p-8 bg-gray-800 text-white">
                <CardContent>
                    <h1 className="text-3xl font-bold mb-4">Login</h1>
                    <form onSubmit={handleSubmit} className="space-y-4">
                        <input
                            type="text"
                            placeholder="API Key"
                            value={apiKey}
                            onChange={(e) => setApiKey(e.target.value)}
                            className="w-full p-2 rounded bg-gray-700 text-white"
                        />
                        <input
                            type="password"
                            placeholder="API Secret"
                            value={apiSecret}
                            onChange={(e) => setApiSecret(e.target.value)}
                            className="w-full p-2 rounded bg-gray-700 text-white"
                        />
                        <Button type="submit" className="bg-blue-500 hover:bg-blue-600 w-full">Login</Button>
                    </form>
                </CardContent>
            </Card>
        </div>
    );
};

export default Login;
