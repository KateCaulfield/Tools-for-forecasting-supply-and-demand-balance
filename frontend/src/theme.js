// src/theme.js
import { createTheme } from '@mui/material/styles';

const darkTheme = createTheme({
    palette: {
        mode: 'dark',
        primary: {
            main: '#90caf9',
        },
        background: {
            default: '#121212',
            paper: '#1e1e1e',
        },
        text: {
            primary: '#ffffff',
        },
    },
});

const slateTheme = createTheme({
    palette: {
        mode: 'light',
        background: {
            default: '#e6f0fa', // светло-голубой фон
            paper: '#ffffff',
        },
        primary: {
            main: '#4caf50', // зелёные кнопки
            contrastText: '#ffffff',
        },
        secondary: {
            main: '#2e7d32',
        },
        text: {
            primary: '#1a1a2e',
            secondary: '#2c3e50',
        },
        error: {
            main: '#f44336',
        },
        divider: '#b0c4de',
    },
});

export default slateTheme;
