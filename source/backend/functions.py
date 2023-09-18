from .database import *


bd = BD()

# ____________________ CONSULTAS ___________________
def consulta_pet(q):
    query = f"""
SELECT
    id,
    nome,
    raca,
    porte,
    sexo,
    observacoes
FROM
 pet
WHERE nome LIKE '%{q}%';
"""
    call = bd.consulta_query(query)
    return call


def consulta_pet_porId(q):
    query = f"""
SELECT
    id,
    nome,
    raca,
    porte,
    sexo,
    observacoes
FROM
 pet
WHERE id = {q};
"""
    call = bd.consulta_query(query)
    return call


def consulta_foto_por_pet(id_p:int):
    query = f"""
SELECT
id,
foto
FROM
 foto
WHERE pet_id = {id_p};
"""
    call = bd.consulta_query(query)
    return call


def consulta_foto_Id(id_p:int):
    query = f"""
SELECT
id
FROM
 foto
WHERE pet_id = {id_p};
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


def consulta_tutores():
    query = f"SELECT id, nome FROM tutor;"
    call = bd.consulta_query(query)
    return call


def consulta_relacao_pets_tutor(q):
    query = f"""
SELECT
    pet.id,
    pet.nome,
    pet.raca,
    pet.porte,
    pet.sexo
FROM
 pet
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


def consulta_pets_com_apenas_um_tutor_por_tutor_id(id_):
    query = f"""
SELECT
	pet_id,
	COUNT(pet_id)
FROM relacao
WHERE pet_id IN (SELECT pet_id FROM relacao WHERE tutor_id = {id_})
GROUP BY pet_id 
HAVING COUNT(pet_id) < 2;
"""
    call = bd.consulta_query(query)
    return call



def consulta_racas():
    query = f"SELECT raca FROM raca ORDER BY raca;"
    call = bd.consulta_query(query)
    return call


# ________________________ ADICOES ____________________________
def add_pet(nome:str, raca:str, porte:str, sexo:str):
    query = f"""
INSERT INTO
    pet (nome, raca, porte, sexo)
VALUES
    (
    '{nome.title()}',
    '{raca}',
    '{porte}',
    '{sexo}'
    )
RETURNING *;
"""
    call = bd.executa_query_com_retorno(query)
    return call


def adiciona_foto(par:tuple):
    '''(bytes, int)'''
    query = f"""
INSERT INTO
    foto (foto, pet_id)
VALUES
    (?, ?)
RETURNING *;
"""
    call = bd.executa_query_com_retorno_Tupla(query, par)
    return call


def add_tutor(nome:str, tel1:str, tel2:str, endereco:str):
    query = f"""
INSERT INTO
    tutor (nome, telefone1, telefone2, endereco)
VALUES
    (
    ?,
    ?,
    ?,
    ?)
RETURNING *;
"""
    tupla = (nome.title(), tel1, tel2, endereco)
    call = bd.executa_query_com_retorno_Tupla(query, tupla)
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
    ('{raca.title().strip()}');
"""
    call = bd.executa_query(query)
    return call


# UPDATES
def atualiza_pet(id:int, nome:str, raca:int, porte:str, sexo:str):
    query = f"""
UPDATE
  pet
SET
    nome = '{nome.title().strip()}',
    raca = '{raca}',
    porte = '{porte}',
    sexo = '{sexo}'
WHERE
  id = {id};
"""
    call = bd.executa_query(query)
    return call


def atualiza_foto(par:tuple):
    '''(bytes, int)'''
    query = f"""
UPDATE
  foto
SET
    foto = ?
WHERE
  pet_id = ?;
"""
    call = bd.executa_query_Tupla(query, par)
    return call


def atualiza_observacao(id:int, data:str):
    query = f"""
UPDATE
  pet
SET
  observacoes = '{data.strip()}'
WHERE
  id = {id};
"""
    call = bd.executa_query(query)
    return call


def atualiza_tutor(id:int, nome:str, tel1:str, tel2:str, endereco:str):
    query = f"""
UPDATE
  tutor
SET
    nome = ?,
    telefone1 = ?,
    telefone2 = ?,
    endereco = ?
WHERE
  id = ?
RETURNING *;
"""
    tupla = (nome.title(), tel1, tel2, endereco, id)
    call = bd.executa_query_com_retorno_Tupla(query, tupla)
    return call


def atualiza_raca(raca:str, raca_nova:str):
    query = f"""
UPDATE
  raca
SET
    raca = '{raca_nova.title().strip()}'
WHERE
  raca = '{raca.title()}';
"""
    call = bd.executa_query(query)
    return call


# REMOCOES
def remove_pet(id:int):
    query = f"DELETE FROM pet WHERE id = {id};"
    call = bd.executa_query(query)
    return call


def remove_foto(foto, id_p:int):
    query = f"DELETE FROM foto WHERE pet_id = {id_p};"
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
    query = f"DELETE FROM raca WHERE raca = '{raca.title()}';"
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
    print(consulta_foto_Id(10))