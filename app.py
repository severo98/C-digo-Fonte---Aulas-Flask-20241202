from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Página Inicial (Login)
@app.route('/')
def login():
    return render_template('login.html')

# Página de Cadastro
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        # Aqui podemos validar os dados, mas por enquanto vamos apenas capturar e redirecionar
        nome = request.form['nome']
        cpf = request.form['cpf']
        email = request.form['email']
        telefone = request.form['telefone']
        endereco = request.form['endereco']
        senha = request.form['senha']
        confirmacao_senha = request.form['confirmacao_senha']

        if senha != confirmacao_senha:
            return "Erro: Senhas não coincidem"
        return redirect(url_for('login'))  # Redireciona para login

    return render_template('cadastro.html')

if __name__ == '__main__':
    app.run(debug=True)
