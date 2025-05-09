// src/pages/LoginPage.js
import React from 'react';
import LoginForm from '../components/LoginForm';
import { useNavigate } from 'react-router-dom';
import { Box, Button } from '@mui/material';

const LoginPage = () => {
    const navigate = useNavigate();

    const handleLoginSuccess = () => {
        navigate('/dashboard');
    };

    return (
        <Box sx={{ mt: 4 }}>
            <LoginForm onLoginSuccess={handleLoginSuccess} />
            <Box sx={{ display: 'flex', justifyContent: 'center', mt: 2 }}>
                <Button variant="text" onClick={() => navigate('/register')}>
                    Нет аккаунта? Зарегистрироваться
                </Button>
            </Box>
        </Box>
    );
};

export default LoginPage;
