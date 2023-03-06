import os
import sqlite3
from sqlite3 import Error

databaseDirectory = os.getcwd() + "\\local\\pythonsqlite.db"

def ExecutarComandoDatabase(comando):
    conn = _obterConexao(databaseDirectory)
    if conn is not None:
        cursor = conn.cursor()
        try:
            cursor.execute(comando)
        except Error as e:
            print("== ERRO AO EXECUTAR COMANDO NO SQLITE ==")
            print(e)

        conn.commit()
        conn.close()

def ExecutarComandoDatabaseComParams(comando, params):
    conn = _obterConexao(databaseDirectory)
    if conn is not None:
        cursor = conn.cursor()
        try:
            cursor.execute(comando, params)
        except Error as e:
            print("== ERRO AO EXECUTAR COMANDO NO SQLITE ==")
            print(e)

        conn.commit()
        conn.close()
        return cursor.lastrowid

def _obterConexao(arquivo_db = databaseDirectory):
    conn = None
    try:
        conn = sqlite3.connect(arquivo_db)
    except Error as e:
        print(e)

    return conn