import React from 'react';
import { Typography, Box, Button } from '@mui/material';
import { useNavigate } from 'react-router-dom';

const DashboardPage = () => {
    const user = JSON.parse(localStorage.getItem('user') || '{}');
    const navigate = useNavigate();

    const handleLogout = () => {
        localStorage.removeItem('token');
        localStorage.removeItem('user');
        navigate('/');
    };

    return (
        <Box sx={{ p: 4 }}>
            <Typography variant="h4" gutterBottom>
                Добро пожаловать, {user.email}
            </Typography>

            <Box sx={{ mt: 2 }}>
                <Button variant="contained" sx={{ mr: 2 }} onClick={() => navigate('/upload')}>
                    Загрузить Excel
                </Button>
                <Button variant="outlined" onClick={() => navigate('/forecast')}>
                    Перейти к прогнозу
                </Button>
            </Box>

            <Box sx={{ mt: 4 }}>
                <Button variant="text" color="error" onClick={handleLogout}>
                    Выйти
                </Button>
            </Box>
        </Box>
    );
};

export default DashboardPage;
