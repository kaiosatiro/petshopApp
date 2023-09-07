import sqlite3
from sqlite3 import Error


class BD:
    def __init__(self):
        self.path = ".\source\database.sqlite"
        self.conexao = self._cria_conexao()
        self._cria_tabelas()


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
        raca INTEGER  NOT NULL,
        porte TEXT NOT NULL,
        sexo TEXT NOT NULL,
        observacoes TEXT,
        FOREIGN KEY(raca) REFERENCES raca(id)
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
        FOREIGN KEY(pet_id) REFERENCES pet(id) ON DELETE CASCADE
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
    

    def executa_query(self, query):
        cursor = self.conexao.cursor()
        try:
            cursor.execute(query)
            self.conexao.commit()
            return 1
        except Error as e:
            return e.sqlite_errorcode


    def consulta_query(self, query):
        cursor = self.conexao.cursor()
        result = None
        try:
            cursor.execute(query)
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
        ('Marley', 1, 'M', 'Macho', 'Teste'),
        ('Cacau', 2, 'P', 'Femea', 'Teste'),
        ('Kiki', 2, 'P', 'Femea', 'Teste');
    """

    cria_tutores = """
    INSERT INTO
    tutor (nome, telefone1, telefone2, endereco)
    VALUES
    ('Chico', '11911111111', '', 'Rua Tal, vila lá 96'),
    ('Neusa', '11922222222', '', 'Rua Tal, vila lá 96'),
    ('Caio', '', '11933333333', 'Rua Tal, vila lá 96'),
    ('TESTE', '', '11999999999', 'Rua Tal, vila lá 96'),
    ('TESTEB', '', '1919191919', 'Rua Tal, vila lá 96');
    """

    cria_racas = """
    INSERT INTO
    raca (raca)
    VALUES
    ('Labrador'),
    ('Negrinha'),
    ('QUIMERA');
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

    query = "SELECT * FROM pet"
    q = bd.consulta_query(query)

    print(q)
    

    