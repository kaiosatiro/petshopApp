import os
import sqlite3
import logging


class DB:
    def __init__(self, path_):
        logging.basicConfig(
            level=logging.INFO,
            encoding='utf-8',
            filename=os.path.join(path_, "log_db.log"),
            format='%(levelname)s - %(asctime)s - %(name)s - %(message)s',
            datefmt='%d-%b-%Y %H:%M:%S'
            )
        
        self.path = os.path.join(path_, "database.sqlite")
        self.connection = self._create_connection()
        self._create_tables()
        self.execute("PRAGMA foreign_keys = TRUE")

    def _create_connection(self):
        conn = None
        try:
            conn = sqlite3.connect(self.path)
            logging.info("Conexão incial com sucesso")
        except sqlite3.Error as e:
            logging.exception("Erro ao criar conexão inicial")
        return conn

    def _create_tables(self):
        pet = """
        CREATE TABLE IF NOT EXISTS pet (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        raca TEXT NOT NULL,
        porte TEXT NOT NULL,
        sexo TEXT NOT NULL,
        observacoes TEXT
        );
        """
        self.execute(pet)

        photo = """
        CREATE TABLE IF NOT EXISTS foto (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        foto BLOB NOT NULL,
        pet_id INTEGER NOT NULL,
        FOREIGN KEY(pet_id) REFERENCES pet(id) ON DELETE CASCADE
        );
        """
        self.execute(photo)

        tutor = """
        CREATE TABLE IF NOT EXISTS tutor (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        telefone1 TEXT,
        telefone2 TEXT,
        frequencia TEXT,
        endereco TEXT
        );
        """

        self.execute(tutor)

        pet_tutor_relation = """
        CREATE TABLE IF NOT EXISTS relacao (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tutor_id INTEGER NOT NULL,
        pet_id INTERGER NOT NULL,
        FOREIGN KEY(tutor_id) REFERENCES tutor(id) ON DELETE CASCADE,
        FOREIGN KEY(pet_id) REFERENCES pet(id) ON DELETE CASCADE,
        UNIQUE(tutor_id, pet_id) ON CONFLICT REPLACE
        );
        """
        self.execute(pet_tutor_relation)

        breed = """
        CREATE TABLE IF NOT EXISTS raca (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        raca TEXT NOT NULL UNIQUE
        );
        """
        self.execute(breed)
    
    #FOR QUERIES WITH ONE PARAMETER, BASICALY ALL THE SEARCHES
    def query(self, query):
        cursor = self.connection.cursor()
        result = None
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except sqlite3.Error as error:
            logging.error(f"{error} - {query}")
            return 'error' , error
    
    #EXECUTIONS WITH PARAMETERS PASSED IN A TUPLE
    def execute_tuple_returning(self, query:str, tp:tuple):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query, tp)
            result = cursor.fetchone()
            self.connection.commit()
            return result
        except sqlite3.Error as error:
            logging.error(f"{error} - {query} - {tp}")
            return 'error', error
        
    #FOR THE IMPORT DATA
    def execute_many_tuple(self, query:str, tp:tuple):
        cursor = self.connection.cursor()
        try:
            cursor.executemany(query, tp)
            self.connection.commit()
            return 1, 'Done!'
        except sqlite3.Error as error:
            logging.error(f"{error} - {query}")
            return 'error', error

    #FOR DELETIONS
    def execute(self, query):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            self.connection.commit()
            return 1, 'Done!'
        except sqlite3.Error as error:
            logging.error(f"{error} - {query}")
            return 'error' , error

