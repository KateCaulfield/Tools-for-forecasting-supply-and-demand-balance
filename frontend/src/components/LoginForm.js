// src/components/LoginForm.js
import React, { useState } from 'react';
import { TextField, Button, Box, Typography } from '@mui/material';
import axios from 'axios';

const LoginForm = ({ onLoginSuccess }) => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();

        try {
            const res = await axios.post('http://localhost:8000/api/users/login/', {
                email,
                password,
            });

            const { access, user } = res.data;
            localStorage.setItem('token', access);
            localStorage.setItem('user', JSON.stringify(user));

            onLoginSuccess(); // перейти дальше
        } catch (err) {
            setError('Неверный логин или пароль');
        }
    };

    return (
        <Box sx={{ maxWidth: 400, mx: 'auto', mt: 8 }}>
            <Typography variant="h5" gutterBottom>Вход</Typography>
            {error && <Typography color="error">{error}</Typography>}
            <form onSubmit={handleSubmit}>
                <TextField
                    label="Email"
                    fullWidth
                    margin="normal"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                />
                <TextField
                    label="Пароль"
                    type="password"
                    fullWidth
                    margin="normal"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                />
                <Button type="submit" variant="contained" fullWidth>Войти</Button>
            </form>
        </Box>
    );
};

export default LoginForm;
