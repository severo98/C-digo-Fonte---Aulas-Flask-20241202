from flask import Flask, render_template

app_Viviane = Flask(__name__, template_folder='t_templates') 
# os templates coloca em outra pasta. 
# Por padrão, fica na pasta templates e não precisa informar no template_folder,
# mas se quiser armazenar em outra pasta indique nesse parâmetro.

@app_Viviane.route("/")       #se no navegador digitar / ou /index
@app_Viviane.route("/index")  
def indice():
    return render_template ("t_index.html") #optei por prefixar com t_ os nomes dos arquivos que usam template

@app_Viviane.route("/contato")
def contato():
    return render_template("t_contato.html") 

@app_Viviane.route("/usuario", defaults={"nome_usuario":"usuário?","nome_profissao":""}) 
def usuarios (nome_usuario, nome_profissao):
    dados_usu = {"nome": "viviane", "profissao":"desenvolvedora"}
    return render_template ("t_usuario.html", nome=nome_usuario, dados = dados_usu)  


#rota /usuarios COM passagem de argumentos
#@app_Viviane.route("/usuario/<nome_usuario>;<nome_profissao>")
#rota /usuarios SEM passagem de argumentos --> definir valor padrão com defaults

if __name__ == "__main__": 
     app_Viviane.run(port = 8000) 