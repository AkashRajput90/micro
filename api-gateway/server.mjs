// apiGateway.js
import express, { json } from 'express';
import cors from 'cors';
const app = express();
const PORT = 8000;

const FLASK_APP_URL = 'http://127.0.0.1:5000';

app.use(cors());
app.use(json());

app.get('/get-flask-app-url', (_req, res) => {
  res.json({ flaskAppUrl: FLASK_APP_URL });
});

app.listen(PORT, () => {
  console.log(`API Gateway running on http://127.0.0.1:${PORT}`);
});
