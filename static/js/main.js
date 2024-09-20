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