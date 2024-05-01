const express = require('express');
const app = express();
const bodyParser = require('body-parser');

// Parse URL-encoded bodies (as sent by HTML forms)
app.use(bodyParser.urlencoded({ extended: true }));

// Parse JSON bodies (as sent by API clients)
app.use(bodyParser.json());

// Serve static files (CSS, images, etc.)
app.use(express.static('public'));

// Simple in-memory database
let users = [];

// Routes
app.get('/', (req, res) => {
    res.sendFile(__dirname + '/create_account.html');
});

app.post('/create-account', (req, res) => {
    const { username, password } = req.body;

    // Simple validation
    if (!username || !password) {
        return res.status(400).send('Username and password are required.');
    }

    // Check if username already exists
    if (users.find(user => user.username === username)) {
        return res.status(400).send('Username already exists.');
    }

    // Create user object
    const newUser = {
        username,
        password
    };

    // Add user to the database
    users.push(newUser);

    // Redirect to login page
    res.redirect('/login');
});

// Start server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
