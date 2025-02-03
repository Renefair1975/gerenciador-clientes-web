import tkinter as tk
from tkinter import messagebox, ttk
from database import listar_clientes, adicionar_cliente, excluir_cliente, atualizar_cliente
from documentos import gerar_contrato, gerar_procuracao, gerar_nota_promissoria, gerar_declaracao, gerar_recibo

# Função para cadastrar clientes
def cadastrar_cliente():
    nome = entry_nome.get()
    cpf = entry_cpf.get()
    telefone = entry_telefone.get()
    email = entry_email.get()
    endereco = entry_endereco.get()

    if nome and cpf and telefone and email and endereco:
        adicionar_cliente(nome, cpf, telefone, email, endereco)
        messagebox.showinfo("Sucesso", f"Cliente {nome} cadastrado com sucesso!")
        limpar_campos()
        atualizar_tabela()
    else:
        messagebox.showwarning("Erro", "Todos os campos são obrigatórios!")

# Função para excluir clientes
def excluir_cliente_selecionado():
    try:
        item_selecionado = tabela.selection()[0]
        cliente_id = tabela.item(item_selecionado)['values'][0]
        excluir_cliente(cliente_id)
        tabela.delete(item_selecionado)
        messagebox.showinfo("Sucesso", "Cliente excluído com sucesso!")
    except IndexError:
        messagebox.showwarning("Erro", "Selecione um cliente para excluir!")

# Função para editar um cliente
def editar_cliente():
    try:
        item_selecionado = tabela.selection()[0]  # Obtém o item selecionado na tabela
        cliente_id = tabela.item(item_selecionado)['values'][0]  # Obtém o ID do cliente

        # Obtém os valores dos campos e remove espaços extras
        nome = entry_nome.get().strip()
        cpf = entry_cpf.get().strip()
        telefone = entry_telefone.get().strip()
        email = entry_email.get().strip()
        endereco = entry_endereco.get().strip()

        # Verifica se algum campo está vazio
        if not nome or not cpf or not telefone or not email or not endereco:
            messagebox.showwarning("Erro", "Todos os campos são obrigatórios!")
            return  # Sai da função se houver campo vazio

        # Atualiza o cliente no banco de dados
        atualizar_cliente(cliente_id, nome, cpf, telefone, email, endereco)
        messagebox.showinfo("Sucesso", f"Cliente {nome} atualizado com sucesso!")

        # Atualiza a tabela e limpa os campos
        atualizar_tabela()
        limpar_campos()

    except IndexError:
        messagebox.showwarning("Erro", "Selecione um cliente para editar!")

# Função para atualizar a tabela de clientes
def atualizar_tabela():
    for item in tabela.get_children():
        tabela.delete(item)

    clientes = listar_clientes()
    for cliente in clientes:
        tabela.insert("", "end", values=cliente)

# Função para gerar os documentos selecionados
def gerar_documentos_cliente():
    try:
        item_selecionado = tabela.selection()[0]
        valores = tabela.item(item_selecionado, "values")

        cliente_id = valores[0]
        nome = valores[1]
        cpf = valores[2]
        telefone = valores[3]
        email = valores[4]
        endereco = valores[5]

        documentos_selecionados = [doc for doc, var in opcoes_documentos.items() if var.get()]

        if not documentos_selecionados:
            messagebox.showwarning("Erro", "Selecione pelo menos um documento para gerar!")
            return

        caminhos_arquivos = []
        for doc in documentos_selecionados:
            if doc == "Contrato":
                caminho = gerar_contrato(cliente_id, nome, cpf, telefone, email, endereco)
            elif doc == "Procuração":
                caminho = gerar_procuracao(cliente_id, nome, cpf, telefone, email, endereco)
            elif doc == "Nota Promissória":
                caminho = gerar_nota_promissoria(cliente_id, nome, cpf, telefone, email, endereco)
            elif doc == "Declaração":
                caminho = gerar_declaracao(cliente_id, nome, cpf, telefone, email, endereco)
            elif doc == "Recibo":
                caminho = gerar_recibo(cliente_id, nome, cpf, telefone, email, endereco)

            caminhos_arquivos.append(caminho)

        messagebox.showinfo("Sucesso", f"Documentos gerados:\n" + "\n".join(caminhos_arquivos))

    except IndexError:
        messagebox.showwarning("Erro", "Selecione um cliente para gerar os documentos!")

# Criando a interface gráfica
root = tk.Tk()
root.title("Gerenciador de Clientes")
root.geometry("700x600")

# Criando Frame do formulário
frame_form = tk.Frame(root)
frame_form.pack(pady=10)

# Criando os campos de entrada
tk.Label(frame_form, text="Nome:").grid(row=0, column=0, padx=5, pady=2, sticky="w")
entry_nome = tk.Entry(frame_form, width=40)
entry_nome.grid(row=0, column=1, padx=5, pady=2)

tk.Label(frame_form, text="CPF:").grid(row=1, column=0, padx=5, pady=2, sticky="w")
entry_cpf = tk.Entry(frame_form, width=40)
entry_cpf.grid(row=1, column=1, padx=5, pady=2)

tk.Label(frame_form, text="Telefone:").grid(row=2, column=0, padx=5, pady=2, sticky="w")
entry_telefone = tk.Entry(frame_form, width=40)
entry_telefone.grid(row=2, column=1, padx=5, pady=2)

tk.Label(frame_form, text="Email:").grid(row=3, column=0, padx=5, pady=2, sticky="w")
entry_email = tk.Entry(frame_form, width=40)
entry_email.grid(row=3, column=1, padx=5, pady=2)

tk.Label(frame_form, text="Endereço:").grid(row=4, column=0, padx=5, pady=2, sticky="w")
entry_endereco = tk.Entry(frame_form, width=40)
entry_endereco.grid(row=4, column=1, padx=5, pady=2)

# Criando botões de ação
btn_cadastrar = tk.Button(frame_form, text="Cadastrar Cliente", command=cadastrar_cliente)
btn_cadastrar.grid(row=5, column=0, pady=10)

btn_editar = tk.Button(frame_form, text="Editar Cliente", command=editar_cliente)
btn_editar.grid(row=5, column=1, pady=10)

btn_excluir = tk.Button(frame_form, text="Excluir Cliente", command=excluir_cliente_selecionado)
btn_excluir.grid(row=6, column=0, columnspan=2, pady=10)

# Criando Frame da tabela
frame_tabela = tk.Frame(root)
frame_tabela.pack(pady=10)

# Criando tabela de clientes
colunas = ("ID", "Nome", "CPF", "Telefone", "Email", "Endereço")
tabela = ttk.Treeview(frame_tabela, columns=colunas, show="headings")

for coluna in colunas:
    tabela.heading(coluna, text=coluna)
    tabela.column(coluna, width=120)

tabela.pack(expand=True, fill="both")

# Criando seleção de documentos
frame_documentos = tk.Frame(root)
frame_documentos.pack(pady=10)

tk.Label(frame_documentos, text="Selecione os documentos a serem gerados:").pack()
opcoes_documentos = {doc: tk.BooleanVar() for doc in ["Contrato", "Procuração", "Nota Promissória", "Declaração", "Recibo"]}
for doc, var in opcoes_documentos.items():
    tk.Checkbutton(frame_documentos, text=doc, variable=var).pack(anchor="w")

btn_gerar_documentos = tk.Button(root, text="Gerar Documentos", command=gerar_documentos_cliente)
btn_gerar_documentos.pack(pady=10)

atualizar_tabela()

root.mainloop()
