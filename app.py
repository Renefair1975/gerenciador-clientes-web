from flask import Flask, render_template, request, redirect, url_for
import os
from database import listar_clientes, adicionar_cliente, excluir_cliente, atualizar_cliente
from documentos import gerar_contrato, gerar_procuracao, gerar_nota_promissoria, gerar_declaracao, gerar_recibo

app = Flask(__name__)

@app.route('/')
def index():
    clientes = listar_clientes()
    return render_template('index.html', clientes=clientes)

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    nome = request.form['nome']
    cpf = request.form['cpf']
    telefone = request.form['telefone']
    email = request.form['email']
    endereco = request.form['endereco']
    
    if nome and cpf and telefone and email and endereco:
        adicionar_cliente(nome, cpf, telefone, email, endereco)
    
    return redirect(url_for('index'))

@app.route('/excluir/<int:cliente_id>')
def excluir(cliente_id):
    excluir_cliente(cliente_id)
    return redirect(url_for('index'))

@app.route('/editar/<int:cliente_id>', methods=['POST'])
def editar(cliente_id):
    nome = request.form['nome']
    cpf = request.form['cpf']
    telefone = request.form['telefone']
    email = request.form['email']
    endereco = request.form['endereco']
    
    atualizar_cliente(cliente_id, nome, cpf, telefone, email, endereco)
    return redirect(url_for('index'))

@app.route('/gerar_documentos/<int:cliente_id>', methods=['POST'])
def gerar_documentos(cliente_id):
    cliente = [c for c in listar_clientes() if c[0] == cliente_id][0]

    documentos_selecionados = request.form.getlist('documentos')

    caminhos = []
    for doc in documentos_selecionados:
        if doc == "Contrato":
            caminho = gerar_contrato(*cliente)
        elif doc == "Procuração":
            caminho = gerar_procuracao(*cliente)
        elif doc == "Nota Promissória":
            caminho = gerar_nota_promissoria(*cliente)
        elif doc == "Declaração":
            caminho = gerar_declaracao(*cliente)
        elif doc == "Recibo":
            caminho = gerar_recibo(*cliente)
        caminhos.append(caminho)

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
