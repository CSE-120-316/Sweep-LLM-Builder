const express = require('express');
const bodyParser = require('body-parser');
const path = require('path'); // To make it work with app.py
const app = express();
const PORT = 3000;

// Middleware
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());
app.use(express.static('public'));

// Temporary in-memory storage for user data
let users = [];

// Route for login authentication
app.post('/login', (req, res) => {
    const { username, password } = req.body;
    const user = users.find(user => user.username === username && user.password === password);
    if (user) {
        //res.redirect('/dropl');
        res.redirect('/hf_to_json2/app.py');
    } else {
        res.redirect('/create_account.html');
    }
});

// Route for user registration
app.post('/register', (req, res) => {
    const { name, lastname, username, password } = req.body;
    // Check if the username is already taken
    if (users.some(user => user.username === username)) {
        return res.status(400).send('Username already exists');
    }
    // Save user data
    users.push({ name, lastname, username, password });
    res.redirect('/intro.html');
});

app.listen(PORT, () => console.log(`Server running on http://localhost:${PORT}`));
