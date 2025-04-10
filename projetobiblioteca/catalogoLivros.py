import sqlite3

def criar_tabela_livros():
    conn = sqlite3.connect("biblioteca.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS livros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT,
            autor TEXT,
            ano INTEGER,
            genero TEXT
        )
    """)
    conn.commit()
    conn.close()

def adicionar_livro(titulo, autor, ano, genero):
    conn = sqlite3.connect("biblioteca.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO livros (titulo, autor, ano, genero)
        VALUES (?, ?, ?, ?)
    """, (titulo, autor, ano, genero))
    conn.commit()
    conn.close()

def listar_livros():
    conn = sqlite3.connect("biblioteca.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM livros")
    livros = cursor.fetchall()

    print("\nCatálogo de Livros:")
    for livro in livros:
        print(f"ID: {livro[0]} | Título: {livro[1]} | Autor: {livro[2]} | Ano: {livro[3]} | Gênero: {livro[4]}")

    conn.close()


criar_tabela_livros()
adicionar_livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954, "Fantasia")
adicionar_livro("O Estrangeiro", "Albert Camus", 2002, "Filosofia")
adicionar_livro("Crime e Castigo", "Fiodor Dostoievski", 1880, "Ficção")
