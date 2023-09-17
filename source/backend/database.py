import sqlite3
from sqlite3 import Error


class BD:
    def __init__(self):
        self.path = ".\source\database.sqlite"
        self.conexao = self._cria_conexao()
        # self._cria_tabelas()
        # self.executa_query("PRAGMA foreign_keys = TRUE")


    def _cria_conexao(self):
        conexao = None
        try:
            conexao = sqlite3.connect(self.path)
            print("Conexão SQLite DB com Sucesso")
        except Error as e:
            print(f"Um erro '{e}' ocorreu")

        return conexao


    def _cria_tabelas(self):
        tabela_pet = """
        CREATE TABLE IF NOT EXISTS pet (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        raca TEXT NOT NULL,
        porte TEXT NOT NULL,
        sexo TEXT NOT NULL,
        observacoes TEXT
        );
        """
        self.executa_query(tabela_pet)

        tabela_pet = """
        CREATE TABLE IF NOT EXISTS foto (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        foto BLOB NOT NULL,
        pet_id INTEGER NOT NULL,
        FOREIGN KEY(pet_id) REFERENCES pet(id) ON DELETE CASCADE
        );
        """
        self.executa_query(tabela_pet)

        tabela_tutor = """
        CREATE TABLE IF NOT EXISTS tutor (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        telefone1 TEXT NOT NULL,
        telefone2 TEXT,
        endereco TEXT
        );
        """
        self.executa_query(tabela_tutor)

        tabela_relacao_petTutor = """
        CREATE TABLE IF NOT EXISTS relacao (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tutor_id INTEGER NOT NULL,
        pet_id INTERGER NOT NULL,
        FOREIGN KEY(tutor_id) REFERENCES tutor(id) ON DELETE CASCADE,
        FOREIGN KEY(pet_id) REFERENCES pet(id) ON DELETE CASCADE,
        UNIQUE(tutor_id, pet_id) ON CONFLICT REPLACE
        );
        """
        self.executa_query(tabela_relacao_petTutor)

        tabela_raca = """
        CREATE TABLE IF NOT EXISTS raca (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        raca TEXT NOT NULL UNIQUE
        );
        """
        self.executa_query(tabela_raca)
    

    def executa_query_com_retorno(self, query):
        cursor = self.conexao.cursor()
        try:
            cursor.execute(query)
            result = cursor.fetchone()
            self.conexao.commit()
            return result
        except Error as e:
            return e.sqlite_errorcode, e.sqlite_errorname
    

    def executa_query(self, query):
        cursor = self.conexao.cursor()
        try:
            cursor.execute(query)
            self.conexao.commit()
            return 1
        except Error as e:
            return e.sqlite_errorcode, e.sqlite_errorname


    def consulta_query(self, query):
        cursor = self.conexao.cursor()
        result = None
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as e:
            return e.sqlite_errorcode
    
    # COM TUPLAS - PASSANDO PARAMETRO

    def executa_query_com_retorno_Tupla(self, query:str, tp:tuple):
        cursor = self.conexao.cursor()
        try:
            cursor.execute(query, tp)
            result = cursor.fetchone()
            self.conexao.commit()
            return result
        except Error as e:
            return e.sqlite_errorcode, e.sqlite_errorname
    

    def executa_query_Tupla(self, query:str, tp:tuple):
        cursor = self.conexao.cursor()
        try:
            cursor.execute(query, tp)
            self.conexao.commit()
            return 1
        except Error as e:
            return e.sqlite_errorcode, e.sqlite_errorname


    def consulta_query_Tupla(self, query:str, tp:tuple):
        cursor = self.conexao.cursor()
        result = None
        try:
            cursor.execute(query, tp)
            result = cursor.fetchall()
            return result
        except Error as e:
            return e.sqlite_errorcode


if __name__ == '__main__':
    bd = BD()
   
    cria_pets = """
        INSERT INTO
        pet (nome, raca, porte, sexo, observacoes)
        VALUES
        ('Marley', 'Labrador', 'M', 'Macho', 'Teste'),
        ('Cacau', 'Bombaim', 'P', 'Femea', 'Teste'),
        ('Kiki', 'Himalaiam', 'P', 'Femea', 'Teste');
    """

    cria_tutores = """
    INSERT INTO
    tutor (nome, telefone1, telefone2, endereco)
    VALUES
    ('Chico', '11911111111', '', 'Rua Tal, vila lá 96'),
    ('Neusa', '11922222222', '', 'Rua Tal, vila lá 96'),
    ('Caio', '', '11933333333', 'Rua Tal, vila lá 96'),
    ('Tata', '', '11999999999', 'Rua Tal, vila lá 96'),
    ('Té', '', '1919191919', 'Rua Tal, vila lá 96');
    """

    cria_racas = """
    INSERT INTO
    raca (raca)
    VALUES
    ('Labrador'),
    ('Negrinha'),
    ('Quimera');
    """

    cria_relacao = """
    INSERT INTO
    relacao (tutor_id, pet_id)
    VALUES
    (1, 1),
    (2, 2),
    (3, 3),
    (2, 3),
    (3, 2),
    (2, 1);
    """
    lista = [cria_pets, cria_tutores, cria_racas, cria_relacao]

    for i in lista:
        bd.executa_query(i)

    query = "SELECT * FROM pet;"
    q = bd.consulta_query(query)

    print(q)
    

    