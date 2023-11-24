__version__ = '1.0'
__author__ = 'Caio Satiro'

import os

from source.backend import DB
from source.main import Main


def example_data(db):
    pets = (
        ('Spike', 'Border Colie', 'Médio', 'Macho', 'Border collie é uma raça canina do tipo collie desenvolvida na região da fronteira anglo-escocesa na Grã-Bretanha para o trabalho de pastorear gado ovino. Popular em seu país de origem, é considerada a raça de cães mais inteligente, de acordo com o livro de Stanley Coren, A Inteligência dos Cães de 1995.'),
        ('Kefir', 'Maine Coon', 'Médio', 'Fêmea', 'Maine Coon é uma raça de gato originária do nordeste dos Estados Unidos. É considerada a raça de pelo mais antiga, além de ser a maior de todas as raças de gato do mundo. Foi reconhecida como raça oficial no estado norte-americano do Maine, onde era famoso pela sua capacidade de caçar ratos e tolerar climas rigorosos')
    )
    tutors = (
        ('John Doe', '1199223344', '11933224433', 'Diário', 'Rua Tal, endereço Lá 99'),
        
        ('Joane Doe', '1199887766', '1199774455', 'Esporático', 'Rua mesma, outro endereço 89')
    )
    breeds = (
        ('Border Colie',),
        ('Maine Coon',)
    )
    relations = (
        (1, 1),
        (1, 2),
        (2, 2)
    )
    recents = (
        (1,),
        (2,)
    )
    def photo_to_blob(dir_):   
        with open(dir_, 'rb') as file:
            blob = file.read()
            return blob
        
    try:
        photo_a = photo_to_blob(os.path.relpath("petApp/images/dog_example.jpg"))
        photo_b = photo_to_blob(os.path.relpath("petApp/images/cat_example.jpg"))
    except FileNotFoundError:
        photo_a = None
        photo_b = None

    photos = (
        (photo_a, 1),
        (photo_b, 2)
    )

    query_pet = "INSERT INTO pet (nome, raca, porte, sexo, observacoes) VALUES (?,?,?,?,?);"
    query_tutor = "INSERT INTO tutor (nome, telefone1, telefone2, frequencia, endereco) VALUES (?,?,?,?,?);"
    query_breed = "INSERT INTO raca (raca) VALUES (?);"
    query_relation = "INSERT INTO relacao (tutor_id, pet_id) VALUES (?,?);"
    query_recent_pet = "INSERT INTO recent_pet (id) VALUES (?);"
    query_recent_tutor = "INSERT INTO recent_tutor (id) VALUES (?);"
    query_photo = "INSERT INTO foto (foto, pet_id) VALUES (?,?);"

    db.execute_many_tuple(query_pet, pets)
    db.execute_many_tuple(query_tutor, tutors)
    db.execute_many_tuple(query_breed, breeds)
    db.execute_many_tuple(query_relation, relations)
    db.execute_many_tuple(query_recent_pet, recents)
    db.execute_many_tuple(query_recent_tutor, recents)
    if photo_a and photo_b:
        db.execute_many_tuple(query_photo, photos)


def main():      
    dB = DB(os.path.dirname(__file__)) # os.getcwd()
    if dB.new_db:
        example_data(dB)
    app = Main(dB)
    app.mainloop()


if __name__ == '__main__':
    main()