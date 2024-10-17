import os
from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY', 'fallback-key')

# Usuários fictícios (pode ser substituído por banco de dados)
usuarios = {
    "usuario": "senha123",
    "admin": "adminpass"
}

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
    # Verifica se o usuário está logado
    if 'username' in session:
        return render_template('index.html')
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Verifica se o usuário existe
        if username in usuarios and usuarios[username] == password:
            session['username'] = username
            return redirect(url_for('home'))
        else:
            return render_template('login.html', error="Usuário ou senha incorretos")
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    # Lógica para exibir e processar o formulário de registro de novos usuários
    return render_template('register.html')

# Página sobre
@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

#promoções
@app.route('/promocoes')
def promocoes():
    return render_template('promo.html')

#curiosidades
@app.route('/curiosidades')
def curiosidades():
    return render_template('curiosidades.html')

#contact
@app.route('/contato', methods=['GET', 'POST'])
def contato():
    if request.method == 'POST':
        nome = request.form['name']
        email = request.form['email']
        mensagem = request.form['message']
        # Lógica para enviar ou processar a mensagem pode ser adicionada aqui
        return "Mensagem enviada com sucesso!"
    return render_template('contact.html')

# Página de produtos
@app.route('/produtos')
def produtos_page():
    return render_template('produtos.html', produtos=produtos)

@app.route('/produto/<produto_nome>')
def produto_detalhes(produto_nome):
    produto = next((p for p in produtos if p['nome'] == produto_nome), None)
    if produto:
        return render_template('produto_detalhes.html', produto=produto)
    else:
        return redirect(url_for('produtos_page'))

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

@app.route('/remover_do_carrinho/<produto_nome>', methods=['POST'])
def remover_do_carrinho(produto_nome):
    # Recupera o carrinho da sessão
    carrinho = session.get('carrinho', [])
    
    # Remove o produto do carrinho, se existir
    carrinho = [item for item in carrinho if item['nome'] != produto_nome]
    
    # Atualiza a sessão com o carrinho modificado
    session['carrinho'] = carrinho
    session.modified = True
    
    return redirect(url_for('carrinho_page'))

@app.route('/limpar_carrinho')
def limpar_carrinho():
    session.pop('carrinho', None)
    return redirect(url_for('carrinho_page', message='Carrinho limpo!'))

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