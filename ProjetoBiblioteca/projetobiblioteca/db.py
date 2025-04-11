import sqlite3

def inicializar_banco():
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

    conn.commit()
    conn.close()
