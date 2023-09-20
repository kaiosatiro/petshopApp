from database import *
import csv

bd = BD()
query_pets = """SELECT nome, raca, porte, sexo, observacoes FROM pet ORDER BY nome;"""
query_tutor = """SELECT nome, telefone1, telefone2, endereco FROM tutor ORDER BY nome;"""
query_raca = "SELECT raca FROM raca ORDER BY raca;"

pet_header = []
tutor_header = []
raca_header = []

pets = []
tutores = []
racas = []

for i in bd.consulta_query("PRAGMA table_info(pet);"):
    pet_header.append(i[1])

for i in bd.consulta_query("PRAGMA table_info(tutor);"):
    tutor_header.append(i[1])

for i in bd.consulta_query("PRAGMA table_info(raca);"):
    raca_header.append(i[1])

pet_header.remove('id')
tutor_header.remove('id')
raca_header.remove('id')

pets.append(pet_header)
for i in bd.consulta_query(query_pets):
    i = list(i)
    pets.append(i)

tutores.append(tutor_header)
for i in bd.consulta_query(query_tutor):
    i = list(i)
    tutores.append(i)

racas.append(raca_header)
for i in bd.consulta_query(query_raca):
    i = list(i)
    racas.append(i)

with open('pets.csv', 'w', newline='') as file:
     writer = csv.writer(file, delimiter=';')
     writer.writerows(pets)

with open('tutores.csv', 'w', newline='') as file:
     writer = csv.writer(file, delimiter=';')
     writer.writerows(tutores)

with open('racas.csv', 'w', newline='') as file:
     writer = csv.writer(file, delimiter=';')
     writer.writerows(racas) 
 






