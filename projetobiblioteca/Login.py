import sqlite3
from cadastro import hash_senha

def fazer_login():
    email = input("Digite seu Email: ")
    senha = input("Digite sua Senha: ")
    senha_hash = hash_senha(senha)

    conn = sqlite3.connect("biblioteca.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM usuarios WHERE email = ? AND senha = ?", (email, senha_hash))
    resultado = cursor.fetchone()

    conn.close()

    if resultado:
        return True  
    else:
        return False
