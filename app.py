from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Função para conectar ao banco de dados
def conectar_banco():
    return sqlite3.connect("clientes.db")

# Página inicial - Lista de Clientes
@app.route("/")
def index():
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    conn.close()
    return render_template("index.html", clientes=clientes)

# Rota para adicionar cliente
@app.route("/adicionar", methods=["POST"])
def adicionar_cliente():
    nome = request.form["nome"]
    cpf = request.form["cpf"]
    telefone = request.form["telefone"]
    email = request.form["email"]
    endereco = request.form["endereco"]

    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO clientes (nome, cpf, telefone, email, endereco) VALUES (?, ?, ?, ?, ?)",
                   (nome, cpf, telefone, email, endereco))
    conn.commit()
    conn.close()

    return redirect(url_for("index"))

# Rota para excluir cliente
@app.route("/excluir/<int:id>")
def excluir_cliente(id):
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM clientes WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
