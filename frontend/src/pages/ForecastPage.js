import React, { useState } from 'react';
import {
    Box, Typography, FormControl, InputLabel, Select, MenuItem, Button
} from '@mui/material';
import axios from 'axios';
import { LineChart, Line, XAxis, YAxis, Tooltip, CartesianGrid, ResponsiveContainer } from 'recharts';
import { useNavigate } from 'react-router-dom';
import html2canvas from 'html2canvas';

const ForecastPage = () => {
    const [resource, setResource] = useState('');
    const [model, setModel] = useState('prophet');
    const [city, setCity] = useState('Все');
    const [data, setData] = useState([]);
    const [error, setError] = useState('');
    const navigate = useNavigate();

    const handleLoadForecast = async () => {
        try {
            const token = localStorage.getItem('token');
            const res = await axios.get(`http://localhost:8000/api/forecast/`, {
                params: { resource, model, city },
                headers: { Authorization: `Bearer ${token}` },
            });
            setData(res.data.forecast);
            setError('');
        } catch (err) {
            setError('Ошибка при получении прогноза');
            setData([]);
        }
        console.log("Model:", model, "City:", city);
    };

    const handleSaveChart = () => {
        const chartElement = document.getElementById('chart-container');
        if (chartElement) {
            html2canvas(chartElement).then((canvas) => {
                const link = document.createElement('a');
                link.download = `forecast_${resource}_${model}_${city}.png`;
                link.href = canvas.toDataURL();
                link.click();
            });
        }
    };

    return (
        <Box sx={{ p: 4 }}>
            <Typography variant="h5" gutterBottom>Прогноз потребления</Typography>

            <FormControl fullWidth sx={{ mb: 2 }}>
                <InputLabel>Ресурс</InputLabel>
                <Select value={resource} onChange={(e) => setResource(e.target.value)}>
                    <MenuItem value="Электроэнергия">Электроэнергия</MenuItem>
                    <MenuItem value="Газ">Газ</MenuItem>
                    <MenuItem value="Нефть">Нефть</MenuItem>
                    <MenuItem value="Уголь">Уголь</MenuItem>
                    <MenuItem value="Теплоэнергия">Теплоэнергия</MenuItem>
                </Select>
            </FormControl>

            <FormControl fullWidth sx={{ mb: 2 }}>
                <InputLabel>Город</InputLabel>
                <Select value={city} onChange={(e) => setCity(e.target.value)}>
                    <MenuItem value="Все">Все</MenuItem>
                    <MenuItem value="Москва">Москва</MenuItem>
                    <MenuItem value="Санкт-Петербург">Санкт-Петербург</MenuItem>
                    <MenuItem value="Казань">Казань</MenuItem>
                    <MenuItem value="Новосибирск">Новосибирск</MenuItem>
                    <MenuItem value="Владивосток">Владивосток</MenuItem>
                    <MenuItem value="Екатеринбург">Екатеринбург</MenuItem>
                    <MenuItem value="Ростов">Ростов</MenuItem>
                    <MenuItem value="Пермь">Пермь</MenuItem>
                    <MenuItem value="Самара">Самара</MenuItem>
                </Select>
            </FormControl>

            <FormControl fullWidth sx={{ mb: 3 }}>
                <InputLabel>Модель</InputLabel>
                <Select value={model} onChange={(e) => setModel(e.target.value)}>
                    <MenuItem value="prophet">Prophet</MenuItem>
                    <MenuItem value="arima">ARIMA</MenuItem>
                    <MenuItem value="rf">Random Forest</MenuItem>
                    <MenuItem value="linear">Linear Regression</MenuItem>
                    <MenuItem value="lstm">LSTM</MenuItem>
                </Select>
            </FormControl>

            <Button variant="contained" onClick={handleLoadForecast} disabled={!resource}>
                Получить прогноз
            </Button>

            {error && <Typography color="error" sx={{ mt: 2 }}>{error}</Typography>}

            {data.length > 0 && (
                <>
                    <Box id="chart-container" sx={{ mt: 4 }}>
                        <ResponsiveContainer width="100%" height={300}>
                            <LineChart data={data}>
                                <CartesianGrid stroke="#ccc" />
                                <XAxis dataKey="ds" />
                                <YAxis />
                                <Tooltip />
                                <Line type="monotone" dataKey="yhat" stroke="#1976d2" strokeWidth={2} />
                            </LineChart>
                        </ResponsiveContainer>
                    </Box>

                    <Button variant="outlined" sx={{ mt: 2 }} onClick={handleSaveChart}>
                        Сохранить график
                    </Button>
                </>
            )}

            <Button variant="text" sx={{ mt: 4 }} onClick={() => navigate('/dashboard')}>
                Назад
            </Button>
        </Box>
    );
};

export default ForecastPage;

