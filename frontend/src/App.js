import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import LoginPage from './pages/LoginPage';
import DashboardPage from './pages/DashboardPage';
import UploadPage from './pages/UploadPage';
import ForecastPage from './pages/ForecastPage';
import EnergyTablePage from './pages/EnergyTablePage';
import RegisterPage from './pages/RegisterPage';

const App = () => {
  return (
      <Router>
        <Routes>
            <Route path="/" element={<LoginPage />} />
            <Route path="/dashboard" element={<DashboardPage />} />
            <Route path="/upload" element={<UploadPage />} />
            <Route path="/forecast" element={<ForecastPage />} />
            <Route path="/energy" element={<EnergyTablePage />} />
            <Route path="/register" element={<RegisterPage />} />
        </Routes>
      </Router>
  );
};

export default App;
