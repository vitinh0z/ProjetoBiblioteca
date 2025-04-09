import sqlite3
import hashlib

# Função para criptografar senha
def hash_senha(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

# Função de cadastro com retorno dos dados
def cadastro():
    usuario = input("Digite nome de Usuario: ")

    while True:
        email = input("Digite seu Email: ")
        emailVerificacao = input("Digite Novamente o email: ")
        if email != emailVerificacao:
            print("Emails não são iguais.")
        else:
            break

    while True:  
        senha = input("Digite uma senha: ")
        senhaVerificacao = input("Digite a senha Novamente: ")
        if senha != senhaVerificacao:
            print("Senhas não são iguais.")
        else:
            break

    senha_hash = hash_senha(senha)
    
    return {"usuario": usuario, "email": email, "senha": senha_hash}

# Função para salvar no banco
def salvar_no_banco(usuario, email, senha):
    conn = sqlite3.connect("biblioteca.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT,
            email TEXT,
            senha TEXT
        )
    """)

    cursor.execute("INSERT INTO usuarios (usuario, email, senha) VALUES (?, ?, ?)",
                   (usuario, email, senha))

    conn.commit()
    conn.close()

# Execução
