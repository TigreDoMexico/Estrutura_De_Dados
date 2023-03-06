import sqlite3
from sqlite3 import Error

def IniciarConexao(arquivo_db):
    conn = None
    try:
        conn = sqlite3.connect(arquivo_db)
        print("Conectado com o Banco SQLITE3 v" + sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()