import csv
import os
from io import BytesIO
from datetime import date
import pandas as pd


def export_data(bd, choice, _dir):
    def save_file(path, data):
        if not data or data == []:
            return 0
        with open(path , 'w', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerows(data)
        if os.path.exists(path):
            return 1
    

    def get_header(table):
        header = []
        for i in bd.query(f"PRAGMA table_info({table});"):
            header.append(i[1])
        header.remove('id')
        return header
    

    def get_values(query):
        data = []
        for i in bd.query(query):
            i = list(i)
            data.append(i)
        return data

        
    def pets(dir_):
        query_pets = """SELECT nome, raca, porte, sexo, observacoes FROM pet ORDER BY nome;""" 
        pet_header = get_header('pet')
        data = get_values(query_pets)
        data.insert(0, pet_header)            
        name = f'pets{date.today()}.csv'
        path = os.path.join(dir_, name)
        return save_file(path, data)
    

    def tutors(dir_):
        query_tutor = """SELECT nome, telefone1, telefone2, frequencia, endereco FROM tutor ORDER BY nome;"""
        tutor_header = get_header('tutor')
        data = get_values(query_tutor)
        data.insert(0, tutor_header)        
        name = f'tutores{date.today()}.csv'
        path = os.path.join(dir_, name)
        return save_file(path, data)


    def breeds(dir_):
        query_breed = "SELECT raca FROM raca ORDER BY raca;"
        breed_header = get_header('raca')
        data = get_values(query_breed)
        data.insert(0, breed_header)
        name = f'racas{date.today()}.csv'
        path = os.path.join(dir_, name)
        return save_file(path, data)
    

    _dir = os.path.realpath(_dir)
    # Execution
    if choice == 'Pets':
        return pets(_dir)
    elif choice == 'Tutores':
        return tutors(_dir)
    elif choice == 'Racas':
        return breeds(_dir)
    elif choice == 'Tudo':
        p = pets(_dir)
        t = tutors(_dir)
        r = breeds(_dir)
        if p and t and r:
            return 1, 'Sucess!'
        else:
            return 'error', "Algo deu errado com ao menos uma das 3 planilhas." 


def import_data(bd, choice, path):
    path =  os.path.realpath(path)
    ext = os.path.splitext(path)[1]
    
    try:
        if ext == ".csv":
            df = pd.read_csv(path, delimiter=';', on_bad_lines='skip', encoding_errors='replace')
        else:
            df = pd.read_excel(path)
    except Exception as ex:
        print(ex)
        return 'errorS', 'Erro na importação do arquivo!'

    data_to_insert = df.to_records(index=False).tolist()

    if choice == 'Pets':
        query = "INSERT INTO pet (nome, raca, porte, sexo, observacoes) VALUES (?,?,?,?,?);"
    elif choice == 'Tutores':
        query = "INSERT INTO tutor (nome, telefone1, telefone2, frequencia, endereco) VALUES (?,?,?,?,?);"
    elif choice == 'Racas':
        query = "INSERT INTO raca (raca) VALUES (?);"

    call = bd.execute_many_tuple(query, data_to_insert)

    return call


def photo_to_blob(dir_):
    with open(dir_, 'rb') as file:
        blob = file.read()
        return blob


def blob_to_photo(blob):
    return BytesIO(blob)





