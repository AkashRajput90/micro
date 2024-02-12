// Header.js
import React from 'react';
import { Link } from 'react-router-dom';
import '../styles/styles.css'; // Adjust the path accordingly

const Header = () => {
  return (
    <header className="header">
      <h1>Your Website Name</h1>
      <nav>
        <ul>
          <li><Link to="/">Home</Link></li>
          <li><Link to="/work">Work</Link></li>
          <li><Link to="/aboutme">About Me</Link></li>
        </ul>
      </nav>
    </header>
  );
}

export default Header;
