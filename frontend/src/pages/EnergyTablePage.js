import React, { useEffect, useState } from 'react';
import { Box, Typography, Button } from '@mui/material';
import { DataGrid } from '@mui/x-data-grid';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const EnergyTablePage = () => {
    const [rows, setRows] = useState([]);
    const [error, setError] = useState('');
    const navigate = useNavigate();

    useEffect(() => {
        const fetchData = async () => {
            try {
                const token = localStorage.getItem('token');
                const res = await axios.get('http://localhost:8000/api/energy/', {
                    headers: { Authorization: `Bearer ${token}` },
                });

                const data = res.data.map((item, index) => ({
                    id: index,
                    ...item,
                }));

                setRows(data);
            } catch (err) {
                setError('Ошибка загрузки данных');
            }
        };

        fetchData();
    }, []);

    const columns = [
        { field: 'resource', headerName: 'Ресурс', width: 150 },
        { field: 'year', headerName: 'Год', width: 100 },
        { field: 'production', headerName: 'Генерация', width: 130 },
        { field: 'import_value', headerName: 'Импорт', width: 130 },
        { field: 'export_value', headerName: 'Экспорт', width: 130 },
        { field: 'consumption', headerName: 'Потребление', width: 150 },
    ];

    return (
        <Box sx={{ p: 4 }}>
            <Typography variant="h5" gutterBottom>Все загруженные данные</Typography>

            {error && <Typography color="error">{error}</Typography>}

            <Box sx={{ height: 500, mt: 2 }}>
                <DataGrid rows={rows} columns={columns} pageSize={10} />
            </Box>

            <Button variant="text" sx={{ mt: 3 }} onClick={() => navigate('/dashboard')}>
                Назад
            </Button>
        </Box>
    );
};

export default EnergyTablePage;
