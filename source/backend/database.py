import sqlite3
from sqlite3 import Error


def cria_conexao(path):
    conexao = None
    try:
        conexao = sqlite3.connect(path)
        print("Conexão SQLite DB com Sucesso")
    except Error as e:
        print(f"Um erro '{e}' ocorreu")

    return conexao


def executa_query(connection, query):
    cursor = conexao.cursor()
    try:
        cursor.execute(query)
        conexao.commit()
        print("Query executa com sucesoo")
    except Error as e:
        print(f"Um erro '{e}' ocorreu")


def cria_tabelas(conexao):
    tabela_pet = """
    CREATE TABLE IF NOT EXISTS pet (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    raca INTEGER  NOT NULL,
    porte TEXT NOT NULL,
    FOREIGN KEY(raca) REFERENCES raca(id)
    );
    """
    executa_query(conexao, tabela_pet)

    tabela_tutor = """
    CREATE TABLE IF NOT EXISTS tutor (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    telefone1 TEXT NOT NULL,
    telefone2 TEXT NOT NULL
    );
    """
    executa_query(conexao, tabela_tutor)

    tabela_relacao_petTutor = """
    CREATE TABLE IF NOT EXISTS pet_tutor (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tutor_id INTEGER NOT NULL,
    pet_id INTERGER NOT NULL,
    FOREIGN KEY(tutor_id) REFERENCES tutor(id),
    FOREIGN KEY(pet_id) REFERENCES pet(id)
    );
    """
    executa_query(conexao, tabela_relacao_petTutor)

    tabela_raca = """
    CREATE TABLE IF NOT EXISTS raca (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    raca TEXT NOT NULL
    );
    """
    executa_query(conexao, tabela_raca)



if __name__ == '__main__':
    conexao = cria_conexao(".\source\database.sqlite")
    cria_tabelas(conexao)