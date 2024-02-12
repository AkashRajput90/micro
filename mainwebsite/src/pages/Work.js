// Work.js
import React, { useState, useEffect } from 'react';

const Work = () => {
  const [flaskAppUrl, setFlaskAppUrl] = useState('');

  useEffect(() => {
    const fetchFlaskAppUrl = async () => {
      try {
        const response = await fetch('http://127.0.0.1:8000/get-flask-app-url');
        if (response.ok) {
          const { flaskAppUrl } = await response.json();
          setFlaskAppUrl(flaskAppUrl);
        } else {
          console.error('Failed to retrieve Flask app URL from the API gateway');
        }
      } catch (error) {
        console.error('Error connecting to the API gateway:', error);
      }
    };

    fetchFlaskAppUrl();
  }, []);

  const redirectToFlaskApp = () => {
    window.location.href = flaskAppUrl;
  };

  return (
    <div>
      <h2>Work Page</h2>
      <p>Explore our work and projects.</p>
      <p>Flask App URL: {flaskAppUrl}</p>
      <button onClick={redirectToFlaskApp}>Go to Flask App</button>
    </div>
  );
};

export default Work;
