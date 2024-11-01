// static/js/script.js
document.getElementById("sendBtn").addEventListener("click", sendMessage);

document.getElementById('userInput').addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        event.preventDefault(); // Prevents the default action (like form submission)
        sendMessage(); // Call the function to send the message
    }
});

function sendMessage() {
    const userInput = document.getElementById("userInput").value;
    document.getElementById("userInput").value = "";  // Clear input field

    const chatbox = document.getElementById("chatbox");
    chatbox.innerHTML += `<div class=" message user-message">${userInput}</div>`;

    fetch('/get_response', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: userInput })
    })
    .then(response => response.json())
    .then(data => {
        chatbox.innerHTML += `<div class="message bot-message">${data.response}</div>`;
        chatbox.scrollTop = chatbox.scrollHeight;
    });
}
function toggleMenu() {
    const menuDropdown = document.getElementById("menuDropdown");
    menuDropdown.classList.toggle("show");
}
// Function to add a message to the chatbox
function addMessage(message, isUser) {
    const chatbox = document.getElementById('chatbox');
    
    const messageDiv = document.createElement('div');
    messageDiv.classList.add(' message '); // Add base message class
    messageDiv.classList.add(isUser ? 'user-message' : 'bot-message'); // Add specific class
    messageDiv.textContent = message;

    chatbox.appendChild(messageDiv);
    chatbox.scrollTop = chatbox.scrollHeight; // Scroll to the bottom
}

// Example usage when the send button is clicked
document.getElementById('sendBtn').addEventListener('click', function() {
    const userInput = document.getElementById('userInput').value;
    if (userInput) {
        addMessage(userInput, true); // Add user message
        document.getElementById('userInput').value = ''; // Clear input field

        // Simulate bot response (replace this with your bot logic)
        setTimeout(() => {
            addMessage("This is a response from the bot.", false); // Add bot message
        }, 1000);
    }
});

// Toggle sidebar visibility
burger.addEventListener("click", () => {
    sidebar.style.left = "0"; // Show sidebar
    sidebar.style.animation = "slideIn 0.3s forwards"; // Animate sidebar
});

closeBtn.addEventListener("click", () => {
    sidebar.style.left = "-250px"; // Hide sidebar
});