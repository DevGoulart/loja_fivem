import os
from flask import Flask, render_template, request, redirect, url_for, session
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY', 'fallback-key')

# Lista de produtos
produtos = [
    {"nome": "Blindagem de Veículos", 'preco': 50.00, "imagem": "image/blindagem.jpg"},
    {"nome": "Textura Personalizada", 'preco': 70.00, "imagem": "image/textura.jpeg"},
    {"nome": "Handling Personalizada", 'preco': 100.00, "imagem": "image/handling.jpg"},
    {"nome": "Pacote Completo", 'preco': 200.00, "imagem": "image/pacote_completo.jpg"}
]

# Página inicial
@app.route('/')
def home():
    return render_template('home.html')

# Página sobre
@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

# Página de produtos
@app.route('/produtos')
def produtos_page():
    return render_template('produtos.html', produtos=produtos)

# Adicionar produto ao carrinho
@app.route('/adicionar_ao_carrinho/<produto_nome>')
def adicionar_ao_carrinho(produto_nome):
    if 'carrinho' not in session:
        session['carrinho'] = []
    
    produto_adicionado = False
    for produto in produtos:
        if produto['nome'] == produto_nome:
            session['carrinho'].append(produto)
            produto_adicionado = True
            break

    if not produto_adicionado:
        return "Produto não encontrado", 404

    session.modified = True
    return redirect(url_for('carrinho_page'))

# Página do carrinho
@app.route('/carrinho')
def carrinho_page():
    carrinho = session.get('carrinho', [])
    total = sum(item['preco'] for item in carrinho)
    return render_template('carrinho.html', carrinho=carrinho, total=total)

# Finalizar pedido
@app.route('/finalizar')
def finalizar_pedido():
    # Recuperar o carrinho da sessão
    carrinho = session.pop('carrinho', [])
    
    # Calcular o total
    total = sum(item['preco'] for item in carrinho)
    
    # Passar os dados para a página de confirmação
    return render_template('confirmacao.html', carrinho=carrinho, total=total)

if __name__ == '__main__':
    app.run(debug=True)