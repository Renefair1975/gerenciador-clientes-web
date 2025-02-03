import sqlite3

# Criando e conectando ao banco de dados
conn = sqlite3.connect("clientes.db")
cursor = conn.cursor()

# Criando a tabela de clientes, se não existir
cursor.execute('''
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cpf TEXT NOT NULL UNIQUE,
    telefone TEXT,
    email TEXT,
    endereco TEXT
);
''')
conn.commit()
conn.close()

# Função para adicionar um novo cliente
def adicionar_cliente(nome, cpf, telefone, email, endereco):
    conn = sqlite3.connect("clientes.db")
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO clientes (nome, cpf, telefone, email, endereco) VALUES (?, ?, ?, ?, ?)",
                       (nome, cpf, telefone, email, endereco))
        conn.commit()
    except sqlite3.IntegrityError:
        print("Erro: CPF já cadastrado.")
    conn.close()

# Função para listar todos os clientes
def listar_clientes():
    conn = sqlite3.connect("clientes.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    conn.close()
    return clientes

# Função para excluir um cliente
def excluir_cliente(cliente_id):
    conn = sqlite3.connect("clientes.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM clientes WHERE id = ?", (cliente_id,))
    conn.commit()
    conn.close()

# Função para atualizar um cliente
import sqlite3

def atualizar_cliente(cliente_id, nome, cpf, telefone, email, endereco):
    conn = sqlite3.connect("clientes.db")
    cursor = conn.cursor()
    
    cursor.execute("""
        UPDATE clientes 
        SET nome = ?, cpf = ?, telefone = ?, email = ?, endereco = ? 
        WHERE id = ?
    """, (nome, cpf, telefone, email, endereco, cliente_id))

    conn.commit()
    conn.close()

# Função para buscar clientes por nome ou CPF
def buscar_clientes(filtro):
    conn = sqlite3.connect("clientes.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clientes WHERE nome LIKE ? OR cpf LIKE ?", (f"%{filtro}%", f"%{filtro}%"))
    clientes = cursor.fetchall()
    conn.close()
    return clientes
