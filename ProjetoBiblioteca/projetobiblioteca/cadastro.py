import sqlite3
import hashlib

def hash_senha(senha):
    """Função para criptografar a senha"""
    return hashlib.sha256(senha.encode()).hexdigest()

def cadastro():
    """Função de cadastro do usuário"""
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

def salvar_no_banco(usuario, email, senha):
    """Função para salvar o cadastro no banco de dados"""
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


if __name__ == "__main__":
    dados = cadastro()
    salvar_no_banco(dados['usuario'], dados['email'], dados['senha'])
    print("Usuário cadastrado com sucesso!")
