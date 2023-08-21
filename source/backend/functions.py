from database import *


bd = BD()

# CONSULTAS
def consulta_pet(q):
    query = f"""
SELECT
    pet.id,
    pet.nome,
    raca.raca,
    pet.porte,
    pet.sexo
FROM
 pet
JOIN raca ON raca.id = pet.raca
WHERE pet.nome LIKE '%{q}%';
"""
    call = bd.consulta_query(query)
    return call


def consulta_tutor(q):
    query = f"SELECT * FROM tutor WHERE nome LIKE '%{q}%';"
    call = bd.consulta_query(query)
    return call


def consulta_relacao_pets_tutor(q):
    query = f"""
SELECT
    pet.id,
    pet.nome,
    raca.raca,
    pet.porte,
    pet.sexo
FROM
 pet
JOIN raca ON raca.id = pet.raca
JOIN relacao ON pet.id = relacao.pet_id
WHERE relacao.tutor_id = {q};
"""
    call = bd.consulta_query(query)
    return call


def consulta_relacao_tutores_pet(q):
    query = f"""
SELECT tutor.*
FROM
 tutor
JOIN relacao ON tutor.id = relacao.tutor_id
WHERE relacao.pet_id = {q};
"""
    call = bd.consulta_query(query)
    return call


def consulta_raca(q):
    query = f"SELECT raca FROM raca;"
    call = bd.consulta_query(query)
    return call


# ADICOES
def add_pet(q):
    ...


def add_tutor(q):
    ...


def add_relacao(q):
    ...


def add_raca(q):
    ...


# UPDATES
def atualiza_pet(q):
    ...


def atualiza_tutor(q):
    ...


# REMOCOES
def remove_pet(q):
    ...


def remove_tutor(q):
    ...


def remove_relacao(q):
    ...


def remove_raca(q):
    ...


if __name__ =='__main__':
    p = consulta_pet('mar')
    print(p)
    t = consulta_tutor('io')
    print(t)
    r = consulta_raca('a')
    print(r)