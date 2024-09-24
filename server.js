const express = require('express');
const path = require('path');
const app = express();

app.use(express.static(path.join(__dirname, 'client', 'build')));

app.get('/api/data', (req,res) => {
    res.json({message : 'Hello from the backend!'});
});

app.get('*', (req,res) => {
    res.sendFile(path.join(__dirname, 'client', 'build', 'index.html'));
});

app.listen(port, () => {
    console.log('Server running at http://localhost:${post}');
});