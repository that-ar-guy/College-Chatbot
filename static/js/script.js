// static/js/script.js
document.getElementById("sendBtn").addEventListener("click", sendMessage);

function sendMessage() {
    const userInput = document.getElementById("userInput").value;
    document.getElementById("userInput").value = "";  // Clear input field

    const chatbox = document.getElementById("chatbox");
    chatbox.innerHTML += `<div class="user-message">${userInput}</div>`;

    fetch('/get_response', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: userInput })
    })
    .then(response => response.json())
    .then(data => {
        chatbox.innerHTML += `<div class="bot-message">${data.response}</div>`;
        chatbox.scrollTop = chatbox.scrollHeight;
    });
}
function toggleMenu() {
    const menuDropdown = document.getElementById("menuDropdown");
    menuDropdown.classList.toggle("show");
}