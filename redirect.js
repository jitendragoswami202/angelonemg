import React, { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

const Redirect = () => {
    const navigate = useNavigate();

    useEffect(() => {
        const urlParams = new URLSearchParams(window.location.search);
        const accessToken = urlParams.get('access_token');
        const refreshToken = urlParams.get('refresh_token');

        if (accessToken && refreshToken) {
            localStorage.setItem('access_token', accessToken);
            localStorage.setItem('refresh_token', refreshToken);
            navigate('/dashboard');
        } else {
            alert('Authentication failed. Please try again.');
            navigate('/login');
        }
    }, [navigate]);

    return (
        <div className="flex justify-center items-center h-screen bg-gray-900 text-white">
            <h1>Redirecting...</h1>
        </div>
    );
};

export default Redirect;
