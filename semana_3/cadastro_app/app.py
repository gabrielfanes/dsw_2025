from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/cadastro", methods=["GET"])
def cadastro():
    return render_template("cadastro.html") 

@app.route("/sucesso", methods=["POST"])
def sucesso():
    nome = request.form.get("nome")
    email = request.form.get("email")
    senha = request.form.get("senha")
    return render_template("sucesso.html", nome=nome, email=email, senha=senha)

if __name__ == "__main__":
    app.run(debug=True)
    
    
