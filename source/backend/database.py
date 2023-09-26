import sqlite3
from sqlite3 import Error
import logging

logging.basicConfig(
    level=logging.INFO,
    encoding='utf-8',
    filename='.\source\log_db.log', 
    # filemode='w',
    format='%(asctime)s - %(message)s',
    datefmt='%d-%b-%Y %H:%M:%S'
)

class BD:
    def __init__(self):
        self.path = ".\source\database.sqlite" #Relative path
        self.conexao = self._cria_conexao()
        self._cria_tabelas()
        self.executa_query("PRAGMA foreign_keys = TRUE")


    def _cria_conexao(self):
        conexao = None
        try:
            conexao = sqlite3.connect(self.path)
            logging.info("Conexão incial com sucesso")
        except Error as e:
            logging.exception("Erro ao criar conexão inicial")
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
        telefone1 TEXT,
        telefone2 TEXT,
        frequencia TEXT,
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
    

    #FOR QUERIES WITH ONE PARAMETER, BASICALY ALL THE SEARCHES
    def consulta_query(self, query):
        cursor = self.conexao.cursor()
        result = None
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as error:
            logging.error(f"{error} - {query}")
            return 'error' , error
    

    #EXECUTIONS WITH PARAMETERS PASSED IN A TUPLE
    def executa_query_com_retorno_Tupla(self, query:str, tp:tuple):
        cursor = self.conexao.cursor()
        try:
            cursor.execute(query, tp)
            result = cursor.fetchone()
            self.conexao.commit()
            return result
        except Error as error:
            logging.error(f"{error} - {query} - {tp}")
            return 'error', error
        

    #FOR THE IMPORT DATA
    def executa_muitos_Tupla(self, query:str, tp:tuple):
        cursor = self.conexao.cursor()
        try:
            cursor.executemany(query, tp)
            self.conexao.commit()
            return 1, 'Done!'
        except Error as error:
            logging.error(f"{error} - {query}")
            return 'error', error


    #FOR DELETIONS
    def executa_query(self, query):
        cursor = self.conexao.cursor()
        try:
            cursor.execute(query)
            self.conexao.commit()
            return 1, 'Done!'
        except Error as error:
            logging.error(f"{error} - {query}")
            return 'error' , error

