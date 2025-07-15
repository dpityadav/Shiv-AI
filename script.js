
async function sendMessage() {
    const userInput = document.getElementById('user-input').value;
    const chatBox = document.getElementById('chat-box');

    if (!userInput) return;

    const userMessage = document.createElement('p');
    userMessage.textContent = "You: " + userInput;
    chatBox.appendChild(userMessage);

    const response = await fetch('/chat', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({message: userInput})
    });

    const data = await response.json();
    const botMessage = document.createElement('p');
    botMessage.textContent = "SHIV: " + data.reply;
    chatBox.appendChild(botMessage);

    document.getElementById('user-input').value = '';
}
