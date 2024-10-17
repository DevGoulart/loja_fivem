const searchInput = document.getElementById('search');
const promoCards = document.querySelectorAll('.promo-card');

// Adiciona o evento de input para filtrar as promoções
searchInput.addEventListener('input', () => {
    const query = searchInput.value.toLowerCase(); // Converte a pesquisa para minúsculo

    promoCards.forEach(card => {
        const text = card.textContent.toLowerCase(); // Converte o conteúdo

        card.style.display = text.includes(query) ? 'block' : 'none';
    });
});
