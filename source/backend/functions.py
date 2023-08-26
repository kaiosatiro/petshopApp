from .database import *


bd = BD()

# CONSULTAS
def consulta_pet(q):
    query = f"""
SELECT
    pet.id,
    pet.nome,
    raca.raca,
    pet.porte,
    pet.sexo,
    pet.observacoes
FROM
 pet
JOIN raca ON raca.id = pet.raca
WHERE pet.nome LIKE '%{q}%';
"""
    call = bd.consulta_query(query)
    return call


def consulta_pet_porId(q):
    query = f"""
SELECT
    pet.id,
    pet.nome,
    raca.raca,
    pet.porte,
    pet.sexo,
    pet.observacoes
FROM
 pet
JOIN raca ON raca.id = pet.raca
WHERE pet.id = {q};
"""
    call = bd.consulta_query(query)
    return call


def consulta_tutor(q):
    query = f"SELECT * FROM tutor WHERE nome LIKE '%{q}%';"
    call = bd.consulta_query(query)
    return call


def consulta_tutor_porId(q):
    query = f"SELECT * FROM tutor WHERE id = {q};"
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


def consulta_racas():
    query = f"SELECT raca FROM raca ORDER BY raca;"
    call = bd.consulta_query(query)
    return call


# ADICOES
def add_pet(nome:str, raca:str, porte:str, sexo:str):
    query = f"""
INSERT INTO
    pet (nome, raca, porte, sexo)
VALUES
    (
    '{nome.title()}',
    (SELECT id FROM raca WHERE raca = '{raca}'),
    '{porte}',
    '{sexo}'
    );
"""
    call = bd.executa_query(query)
    return call


def add_tutor(nome:str, tel1:str, tel2:str):
    query = f"""
INSERT INTO
    tutor (nome, telefone1, telefone2)
VALUES
    (
    '{nome.title()}',
    '{tel1}',
    '{tel2}'
    );
"""
    call = bd.executa_query(query)
    return call


def add_relacao(t_id:int, p_id:int):
    check = f"SELECT COUNT(id) FROM relacao WHERE pet_id = {p_id};"
    if bd.consulta_query(check)[0][0] > 2:
        return 0, "Pet já tem dois tutores"
    else:            
        query = f"""
    INSERT INTO
        relacao (tutor_id, pet_id)
    VALUES
        (
        {t_id},
        {p_id}
        );
    """
        call = bd.executa_query(query)
        return call


def add_raca(raca:str):
    query = f"""
INSERT INTO
    raca (raca)
VALUES
    ('{raca.title()}');
"""
    call = bd.executa_query(query)
    return call


# UPDATES
def atualiza_pet(id:int, nome:str, raca:int, porte:str, sexo:str):
    query = f"""
UPDATE
  pet
SET
    nome = '{nome}',
    raca = (SELECT id FROM raca WHERE raca = '{raca}'),
    porte = '{porte}',
    sexo = '{sexo}'
WHERE
  id = {id};
"""
    call = bd.executa_query(query)
    return call


def atualiza_observacao(id:int, data:str):
    query = f"""
UPDATE
  pet
SET
  observacoes = '{data}'
WHERE
  id = {id};
"""
    call = bd.executa_query(query)
    return call


def atualiza_tutor(id:str, nome:str, tel1:str, tel2:str):
    query = f"""
UPDATE
  tutor
SET
    nome = '{nome}',
    telefone1 = '{tel1}',
    telefone2 = '{tel2}'
WHERE
  id = {id};
"""
    call = bd.executa_query(query)
    return call


# REMOCOES
def remove_pet(id:int):
    query = f"DELETE FROM pet WHERE id = {id};"
    call = bd.executa_query(query)
    return call


def remove_tutor(id:int):
    query = f"DELETE FROM tutor WHERE id = {id};"
    call = bd.executa_query(query)
    return call


def remove_relacao(id_p:int, id_t:int):
    query = f"DELETE FROM relacao WHERE pet_id = {id_p} and tutor_id = {id_t};"
    call = bd.executa_query(query)
    return call

def remove_raca(raca:str):
    query = f"DELETE FROM raca WHERE raca = '{raca}';"
    call = bd.executa_query(query)
    return call


if __name__ =='__main__':
    # p = consulta_pet('mar')
    # print(p)
    # t = consulta_tutor('io')
    # print(t)
    # r = consulta_raca('a')
    # print(r)
    # add = add_pet('urso', 'Labrador', 'M', 'Macho')
    # print(add)
    # p = consulta_pet('urs')
    # print(p)
    # q = bd.consulta_query(f"SELECT COUNT(id) FROM relacao WHERE pet_id = 2;")
    # print(type(q[0][0]))
    ...