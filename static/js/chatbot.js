const openChatBtn = document.getElementById('open-chat');
const closeChatBtn = document.getElementById('close-chat');
const chatContainer = document.getElementById('chatbot');
const chatBody = document.getElementById('chat-body');
const userInput = document.getElementById('user-input');
const sendBtn = document.getElementById('send-btn');

// Abrir o chat
openChatBtn.addEventListener('click', () => {
    chatContainer.style.display = 'flex';
    openChatBtn.style.display = 'none';
});

// Fechar o chat
closeChatBtn.addEventListener('click', () => {
    chatContainer.style.display = 'none';
    openChatBtn.style.display = 'block';
});

// Enviar mensagem
sendBtn.addEventListener('click', () => handleUserMessage());
userInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') handleUserMessage();
});

// Processar a mensagem do usuário
function handleUserMessage() {
    const message = userInput.value.trim();
    if (message) {
        addMessage(message, 'user');
        userInput.value = '';
        botResponse(message);
    }
}

// Adicionar mensagem no chat
function addMessage(text, sender) {
    const messageDiv = document.createElement('div');
    messageDiv.classList.add('message', sender);
    messageDiv.textContent = text;
    chatBody.appendChild(messageDiv);
    chatBody.scrollTop = chatBody.scrollHeight; // Rola para o final
}

// Simular resposta do bot
function botResponse(userMessage) {
    let response;

    switch (userMessage.toLowerCase()) {
        case 'promoção':
            response = 'Visite nossa aba de promoções para conferir ofertas especiais!';
            break;
        case 'produtos':
            response = 'Visite nossa aba de produtos para conferir!';
            break;
        case 'contato':
            response = 'Precisa de ajuda? Vá para a página de contato!';
            break;
        case 'olá':
        case 'oi':
            response = 'Olá! Como posso ajudar você hoje?';
            break;
        default:
            response = 'Desculpe, não entendi. Pode tentar outra pergunta?';
    }

    setTimeout(() => addMessage(response, 'bot'), 500);
}
