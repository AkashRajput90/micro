// App.js
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Header from './components/Header';  // Add this import
import Footer from './components/Footer';  // Add this import
import Home from './components/Home';
import Work from './pages/Work';
import AboutMe from './pages/AboutMe';

const App = () => {
  return (
    <Router>
      <Header /> {/* Add header */}
      
      <Routes>
        <Route path="/work" element={<Work />} />
        <Route path="/aboutme" element={<AboutMe />} />
        <Route path="/" element={<Home />} />
      </Routes>
      <Footer /> {/* Add footer */}
    </Router>
  );
}

export default App;
