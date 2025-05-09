import React, { useState } from 'react';
import {
    TextField, Button, Box, Typography, FormControl, InputLabel, Select, MenuItem
} from '@mui/material';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const RegisterForm = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [role, setRole] = useState('User');
    const [error, setError] = useState('');
    const navigate = useNavigate();

    const handleRegister = async (e) => {
        e.preventDefault();

        try {
            await axios.post('http://localhost:8000/api/users/register/', {
                email, password, role
            });

            navigate('/');
        } catch (err) {
            setError('Ошибка регистрации. Возможно, пользователь уже существует.');
        }
    };

    return (
        <Box sx={{ maxWidth: 400, mx: 'auto', mt: 8 }}>
            <Typography variant="h5" gutterBottom>Регистрация</Typography>
            {error && <Typography color="error">{error}</Typography>}

            <form onSubmit={handleRegister}>
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
                <FormControl fullWidth margin="normal">
                    <InputLabel>Роль</InputLabel>
                    <Select value={role} onChange={(e) => setRole(e.target.value)}>
                        <MenuItem value="User">User</MenuItem>
                        <MenuItem value="Editor">Editor</MenuItem>
                        <MenuItem value="Admin">Admin</MenuItem>
                    </Select>
                </FormControl>
                <Button type="submit" variant="contained" fullWidth>Зарегистрироваться</Button>
            </form>

            <Button variant="text" sx={{ mt: 2 }} onClick={() => navigate('/')}>
                Уже есть аккаунт? Войти
            </Button>
        </Box>
    );
};

export default RegisterForm;
