const express = require('express');
const path = require('path');
require('dotenv').config();
const cors = require('cors');

const app = express();
const port = 3001;

// Serve static files from the 'public' directory
app.use(express.static(path.join(__dirname, 'public')));

app.use(cors());

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'otp.html'));
});

app.post('/send-otp', (req, res) => {
    // Implement send-otp logic here
});

app.post('/verify-otp', (req, res) => {
    // Implement verify-otp logic here
});

app.listen(port, () => {
    console.log(`Server running on http://localhost:${port}`);
});


