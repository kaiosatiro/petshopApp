# ____________________ CONSULTAS ___________________
def consulta_pet(bd, q:str):
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
    call = bd.consulta_query(query)
    return call


def consulta_pet_porId(bd, q:int):
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


def consulta_foto_por_pet(bd, id_p:int):
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


def consulta_foto_Id(bd, id_p:int):
    query = f"""
SELECT
id
FROM
 foto
WHERE pet_id = {id_p};
"""
    call = bd.consulta_query(query)
    return call


def consulta_tutor(bd, q):
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
    call = bd.consulta_query(query)
    return call


def consulta_tutor_porId(bd, q:int):
    query = f"SELECT * FROM tutor WHERE id = {q};"
    call = bd.consulta_query(query)
    return call


def consulta_tutores(bd):
    query = f"SELECT id, nome FROM tutor;"
    call = bd.consulta_query(query)
    return call


def consulta_relacao_pets_tutor(bd, id_:int):
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
    call = bd.consulta_query(query)
    return call


def consulta_relacao_tutores_pet(bd, q:int):
    query = f"""
SELECT tutor.*
FROM
 tutor
JOIN relacao ON tutor.id = relacao.tutor_id
WHERE relacao.pet_id = {q};
"""
    call = bd.consulta_query(query)
    return call


# def consulta_contagem_tutor_por_pet(bd, pet_id):
#     check = f"SELECT COUNT(id) FROM relacao WHERE pet_id = {pet_id};"
#     if bd.consulta_query(check)[0][0] > 2:
#         return 0, "Pet já tem dois tutores"
#     else:
#         return 1


def consulta_pets_com_apenas_um_tutor_por_tutor_id(bd, id_:int):
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


def consulta_racas(bd):
    query = f"SELECT raca FROM raca ORDER BY raca;"
    call = bd.consulta_query(query)
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
    call = bd.executa_query_com_retorno_Tupla(query, tupla)
    return call


def adiciona_foto(bd, blob:bytes, pet_id:int):
    '''(bytes, int)'''
    tupla = (blob, pet_id)
    query = f"""
INSERT INTO
    foto (foto, pet_id)
VALUES
    (?, ?)
RETURNING *;
"""
    call = bd.executa_query_com_retorno_Tupla(query, tupla)
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
    call = bd.executa_query_com_retorno_Tupla(query, tupla)
    return call


def add_relacao(bd, t_id:int, p_id:int):
    tupla = (t_id, p_id)      
    query = f"""
INSERT INTO
    relacao (tutor_id, pet_id)
VALUES
    (?, ?)
RETURNING *;
"""
    call = bd.executa_query_com_retorno_Tupla(query, tupla)
    return call


def add_raca(bd, raca:str):
    tupla = (raca.title(),)
    query = f"""
INSERT INTO
    raca (raca)
VALUES
    (?)
RETURNING raca;
"""
    call = bd.executa_query_com_retorno_Tupla(query, tupla)
    return call


# UPDATES
def atualiza_pet(bd, id_:int, nome:str, raca:int, porte:str, sexo:str):
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
    call = bd.executa_query_com_retorno_Tupla(query, tupla)
    return call


def atualiza_foto(bd, blob:bytes, pet_id:int):
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
    call = bd.executa_query_com_retorno_Tupla(query, tupla)
    return call


def atualiza_observacao(bd, id_:int, data:str):
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
    call = bd.executa_query_com_retorno_Tupla(query, tupla)
    return call


def atualiza_tutor(bd, id:int, nome:str, tel1:str, tel2:str, frequencia:str, endereco:str):
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
    call = bd.executa_query_com_retorno_Tupla(query, tupla)
    return call


def atualiza_raca(bd, raca:str, raca_nova:str):
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
    call = bd.executa_query_com_retorno_Tupla(query, tupla)
    return call


# REMOCOES
def remove_pet(bd, id:int):
    query = f"DELETE FROM pet WHERE id = {id};"
    call = bd.executa_query(query)
    return call


def remove_foto(bd, id_p:int):
    query = f"DELETE FROM foto WHERE pet_id = {id_p};"
    call = bd.executa_query(query)
    return call


def remove_tutor(bd, id:int):
    query = f"DELETE FROM tutor WHERE id = {id};"
    call = bd.executa_query(query)
    return call


def remove_relacao(bd, id_p:int, id_t:int):
    query = f"DELETE FROM relacao WHERE pet_id = {id_p} and tutor_id = {id_t};"
    call = bd.executa_query(query)
    return call


def remove_raca(bd, raca:str):
    query = f"DELETE FROM raca WHERE raca = '{raca}';"
    call = bd.executa_query(query)
    return call
