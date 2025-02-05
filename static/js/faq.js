document.querySelectorAll('.faq-question').forEach(question => {
    question.addEventListener('click', () => {
        const answer = question.nextElementSibling;

        // Fecha todas as respostas abertas, exceto a clicada
        document.querySelectorAll('.faq-answer').forEach(item => {
            if (item !== answer) {
                item.style.maxHeight = null;
            }
        });

        // Alterna entre abrir e fechar a resposta clicada
        if (answer.style.maxHeight) {
            answer.style.maxHeight = null;
        } else {
            answer.style.maxHeight = answer.scrollHeight + "px";
        }
    });
});
