// frontend/index.jsx
import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './src/App';
import { ThemeProvider } from '@mui/material/styles';
import theme from './src/theme';
import { AppProvider } from './src/context';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <ThemeProvider theme={theme}>
        <AppProvider>
            <App />
        </AppProvider>
    </ThemeProvider>
);
