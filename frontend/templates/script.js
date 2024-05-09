// Ashley Gonzalez Perez May 8, 2024

document.addEventListener('DOMContentLoaded', function () {
    var chatBox = document.getElementById('chat-box');
    var userInput = document.getElementById('user-input');
    var sendButton = document.getElementById('send-button');

    function addMessage(message, sender) {
        var messageDiv = document.createElement('div');
        messageDiv.className = 'message';
        messageDiv.innerHTML = '<strong>' + sender + ':</strong> ' + message;
        chatBox.appendChild(messageDiv);
        chatBox.scrollTop = chatBox.scrollHeight; // Auto-scroll to bottom
    }

    sendButton.addEventListener('click', function () {
        var message = userInput.value.trim();
        if (message !== '') {
            addMessage(message, 'You');
            userInput.value = '';
            // Here you can send the message to the server or process it further
            // For demonstration purposes, we're just adding the message to the chat box
        }
    });

    // Example of receiving a message (for demonstration purposes)
    setTimeout(function () {
        addMessage("Hello! How can I help you?", "Assistant");
    }, 1000);
});
