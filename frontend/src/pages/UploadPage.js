import React, { useState, useEffect } from 'react';
import { Box, Typography, Button, Input, Alert, Stack } from '@mui/material';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const UploadPage = () => {
    const [file, setFile] = useState(null);
    const [message, setMessage] = useState('');
    const navigate = useNavigate();

    const handleFileChange = (e) => {
        setFile(e.target.files[0]);
        setMessage('');
    };

    const handleUpload = async () => {
        if (!file) return;

        const formData = new FormData();
        formData.append('file', file);

        try {
            const token = localStorage.getItem('token');
            const res = await axios.post('http://localhost:8000/api/energy/upload/', formData, {
                headers: {
                    'Authorization': `Bearer ${token}`,
                    'Content-Type': 'multipart/form-data',
                },
            });

            setMessage(`✅ ${res.data.message}`);
        } catch (err) {
            setMessage('❌ Ошибка при загрузке файла');
        }
    };

    useEffect(() => {
        if (message) {
            const timer = setTimeout(() => setMessage(''), 2000);
            return () => clearTimeout(timer);
        }
    }, [message]);

    return (
        <Box sx={{ maxWidth: 500, mx: 'auto', mt: 8, textAlign: 'center' }}>
            <Typography variant="h5" gutterBottom>Загрузка Excel-файла</Typography>

            <Input type="file" onChange={handleFileChange} />

            {message && (
                <Alert sx={{ mt: 2 }} severity={message.startsWith('✅') ? 'success' : 'error'}>
                    {message}
                </Alert>
            )}

            <Stack spacing={2} mt={2}>
                <Button onClick={handleUpload} variant="contained">Загрузить</Button>
                <Button variant="text" onClick={() => navigate('/dashboard')}>Назад</Button>
            </Stack>
        </Box>
    );
};

export default UploadPage;
