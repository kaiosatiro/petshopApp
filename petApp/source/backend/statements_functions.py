# ____________________ CONSULTAS ___________________
def pet_query(bd, q:str):
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
WHERE nome LIKE '%{q}%'
ORDER BY nome;
"""
    call = bd.query(query)
    return call


def pet_query_by_id(bd, q:int):
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
    call = bd.query(query)
    return call


def query_photo_by_pet_id(bd, id_p:int):
    query = f"""
SELECT
id,
foto
FROM
 foto
WHERE pet_id = {id_p};
"""
    call = bd.query(query)
    return call


def quey_photo_by_id(bd, id_p:int):
    query = f"""
SELECT
id
FROM
 foto
WHERE pet_id = {id_p};
"""
    call = bd.query(query)
    return call


def query_tutor(bd, q):
    query = f"""
SELECT
    id,
    nome,
    telefone1,
    telefone2,
    frequencia
FROM 
    tutor 
WHERE 
    nome 
LIKE '%{q}%' 
ORDER BY nome;
"""
    call = bd.query(query)
    return call


def query_tutor_by_id(bd, q:int):
    query = f"SELECT * FROM tutor WHERE id = {q};"
    call = bd.query(query)
    return call


def query_many_tutors(bd):
    query = f"SELECT id, nome FROM tutor;"
    call = bd.query(query)
    return call


def query_pet_tutor_relation(bd, id_:int):
    query = f"""
SELECT
    pet.id,
    pet.nome,
    pet.raca
FROM
 pet
JOIN relacao ON pet.id = relacao.pet_id
WHERE relacao.tutor_id = {id_}
ORDER BY pet.nome;
"""
    call = bd.query(query)
    return call


def query_tutor_pet_relation(bd, pet_id:int):
    query = f"""
SELECT tutor.*
FROM
 tutor
JOIN relacao ON tutor.id = relacao.tutor_id
WHERE relacao.pet_id = {pet_id};
"""
    call = bd.query(query)
    return call


# def consulta_contagem_tutor_por_pet(bd, pet_id):
#     check = f"SELECT COUNT(id) FROM relacao WHERE pet_id = {pet_id};"
#     if bd.query(check)[0][0] > 2:
#         return 0, "Pet já tem dois tutores"
#     else:
#         return 1


def query_pets_with_only_one_tutor(bd, id_:int):
    query = f"""
SELECT
	pet_id,
	COUNT(pet_id)
FROM relacao
WHERE pet_id IN (SELECT pet_id FROM relacao WHERE tutor_id = {id_})
GROUP BY pet_id 
HAVING COUNT(pet_id) < 2;
"""
    call = bd.query(query)
    return call


def query_breeds(bd):
    query = f"SELECT raca FROM raca ORDER BY raca;"
    call = bd.query(query)
    return call


def query_recent_pet(bd):
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
WHERE id in (SELECT id from recent_pet);
"""
    call = bd.query(query)
    return call


def query_recent_tutor(bd):
    query = f"""
SELECT
    id,
    nome,
    telefone1,
    telefone2,
    frequencia
FROM
    tutor
WHERE id in (SELECT id from recent_tutor);
"""
    call = bd.query(query)
    return call

# ________________________ ADICOES ____________________________
def add_pet(bd, nome:str, raca:str, porte:str, sexo:str):
    tupla = (nome.title(), raca, porte, sexo)
    query = f"""
INSERT INTO
    pet (nome, raca, porte, sexo)
VALUES
    (?, ?, ?, ?)
RETURNING *;
"""
    call = bd.execute_tuple_returning(query, tupla)
    return call


def add_photo(bd, blob:bytes, pet_id:int):
    '''(bytes, int)'''
    tupla = (blob, pet_id)
    query = f"""
INSERT INTO
    foto (foto, pet_id)
VALUES
    (?, ?)
RETURNING *;
"""
    call = bd.execute_tuple_returning(query, tupla)
    return call


def add_tutor(bd, nome:str, tel1:str, tel2:str, frequencia:str, endereco:str):
    tupla = (nome.title(), tel1, tel2, frequencia, endereco)
    query = f"""
INSERT INTO
    tutor (nome, telefone1, telefone2, frequencia, endereco)
VALUES
    (?, ?, ?, ?, ?)
RETURNING *;
"""
    call = bd.execute_tuple_returning(query, tupla)
    return call


def add_relation(bd, t_id:int, p_id:int):
    tupla = (t_id, p_id)      
    query = f"""
INSERT INTO
    relacao (tutor_id, pet_id)
VALUES
    (?, ?)
RETURNING *;
"""
    call = bd.execute_tuple_returning(query, tupla)
    return call


def add_breed(bd, raca:str):
    tupla = (raca.title(),)
    query = f"""
INSERT INTO
    raca (raca)
VALUES
    (?)
RETURNING raca;
"""
    call = bd.execute_tuple_returning(query, tupla)
    return call


def insert_recent_pet(bd, id_list:list):
    list_ = [(id_,) for id_ in id_list]
    query = f"""
INSERT INTO
    recent_pet (id)
VALUES
    (?);
"""
    call = bd.execute_many_tuple(query, list_)


def insert_recent_tutor(bd, id_list:list):
    list_ = [(id_,) for id_ in id_list]
    query = f"""
INSERT INTO
    recent_tutor (id)
VALUES
    (?);
"""
    call = bd.execute_many_tuple(query, list_)


# UPDATES
def pet_update(bd, id_:int, nome:str, raca:int, porte:str, sexo:str):
    tupla = (nome.title(), raca, porte, sexo, id_)
    query = f"""
UPDATE
  pet
SET
    nome = ?,
    raca = ?,
    porte = ?,
    sexo = ?
WHERE
  id = ?
RETURNING *
"""
    call = bd.execute_tuple_returning(query, tupla)
    return call


def photo_update(bd, blob:bytes, pet_id:int):
    '''(bytes, int)'''
    tupla = (blob, pet_id)
    query = f"""
UPDATE
  foto
SET
    foto = ?
WHERE
  pet_id = ?
RETURNING id;
"""
    call = bd.execute_tuple_returning(query, tupla)
    return call


def update_observation(bd, id_:int, data:str):
    tupla = (data, id_)
    query = f"""
UPDATE
  pet
SET
  observacoes = ?
WHERE
  id = ?
RETURNING observacoes;
"""
    call = bd.execute_tuple_returning(query, tupla)
    return call


def update_tutor(bd, id:int, nome:str, tel1:str, tel2:str, frequencia:str, endereco:str):
    tupla = (nome.title(), tel1, tel2, frequencia, endereco, id)
    query = f"""
UPDATE
  tutor
SET
    nome = ?,
    telefone1 = ?,
    telefone2 = ?,
    frequencia = ?,
    endereco = ?
WHERE
  id = ?
RETURNING *;
"""
    call = bd.execute_tuple_returning(query, tupla)
    return call


def update_breed(bd, raca:str, raca_nova:str):
    tupla = (raca_nova.title(), raca)
    query = f"""
UPDATE
  raca
SET
    raca = ?
WHERE
  raca = ?
RETURNING raca;
"""
    call = bd.execute_tuple_returning(query, tupla)
    return call


# REMOCOES
def remove_pet(bd, id:int):
    query = f"DELETE FROM pet WHERE id = {id};"
    call = bd.execute(query)
    return call


def remove_photo(bd, id_p:int):
    query = f"DELETE FROM foto WHERE pet_id = {id_p};"
    call = bd.execute(query)
    return call


def remove_tutor(bd, id:int):
    query = f"DELETE FROM tutor WHERE id = {id};"
    call = bd.execute(query)
    return call


def remove_relation(bd, id_p:int, id_t:int):
    query = f"DELETE FROM relacao WHERE pet_id = {id_p} and tutor_id = {id_t};"
    call = bd.execute(query)
    return call


def remove_breed(bd, raca:str):
    query = f"DELETE FROM raca WHERE raca = '{raca}';"
    call = bd.execute(query)
    return call


def remove_recent_pet(bd):
    query = f"DELETE FROM recent_pet;"
    call = bd.execute(query)
    return call


def remove_recent_tutor(bd):
    query = f"DELETE FROM recent_tutor;"
    call = bd.execute(query)
    return call