document.addEventListener('DOMContentLoaded', () => {
    const notification = document.querySelector('.notification');
    if (notification) {
        // Força o navegador a aplicar as transições CSS
        requestAnimationFrame(() => {
            requestAnimationFrame(() => {
                notification.classList.add('show');
            });
        });

        // Remove a notificação após um período
        setTimeout(() => {
            notification.classList.remove('show');
            setTimeout(() => {
                notification.remove();
            }, 500); // Duração da transição de saída
        }, 3000); // Duração da exibição
    }
});

document.addEventListener('DOMContentLoaded', () => {
    const loadingIndicator = document.getElementById('loading-indicator');

    // Função para mostrar o indicador de carregamento
    function showLoadingIndicator() {
        loadingIndicator.style.display = 'block';
    }

    // Função para ocultar o indicador de carregamento
    function hideLoadingIndicator() {
        loadingIndicator.style.display = 'none';
    }

    // Exibir o indicador ao carregar a página
    showLoadingIndicator();

    // Ocultar o indicador quando a página estiver completamente carregada
    window.addEventListener('load', hideLoadingIndicator);

    // Se você estiver fazendo requisições assíncronas (como a adição ao carrinho), use as funções abaixo
    const addToCartButtons = document.querySelectorAll('form[action="/add_to_cart"]');

    addToCartButtons.forEach(button => {
        button.addEventListener('submit', (event) => {
            event.preventDefault();
            const form = event.target;

            // Mostrar o indicador de carregamento antes da requisição
            showLoadingIndicator();

            fetch('/add_to_cart', {
                method: 'POST',
                body: new URLSearchParams(new FormData(form)),
            }).then(response => {
                if (response.ok) {
                    showTemporaryNotification('Produto adicionado ao carrinho!');
                }
            }).finally(() => {
                // Ocultar o indicador após a requisição
                hideLoadingIndicator();
            });
        });
    });
});
