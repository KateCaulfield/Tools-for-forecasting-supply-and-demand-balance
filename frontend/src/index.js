// src/index.js
import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import { ThemeProvider } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';
import slateTheme from './theme';

const root = ReactDOM.createRoot(document.getElementById('root'));

root.render(
    <ThemeProvider theme={slateTheme}>
        <CssBaseline />
        <App />
    </ThemeProvider>
);


