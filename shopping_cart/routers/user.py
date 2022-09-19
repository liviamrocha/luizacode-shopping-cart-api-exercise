from shopping_cart.schemas.user import *
from shopping_cart.repository.users import *
from shopping_cart.repository.adresses import *
from shopping_cart.repository.products import *
from shopping_cart.repository.carts import *
from fastapi import APIRouter

router = APIRouter()

OK = "OK"
FALHA = "FALHA"

# Criar um usuário,
# se tiver outro usuário com o mesmo ID retornar falha, 
# se o email não tiver o @ retornar falha, 
# senha tem que ser maior ou igual a 3 caracteres, 
# senão retornar OK
@router.post("/usuario/")
async def criar_usuário(usuario: Usuario):
    if UserValidation(usuario).valid_user():
        User.add_user(usuario)
        return OK
    return FALHA


# Se o id do usuário existir, retornar os dados do usuário
# senão retornar falha
@router.get("/usuario/")
async def retornar_usuario(id: int):
    if UserValidation.valid_id(id):
        return User.get_user_by_id(id)
    return FALHA


# Se existir um usuário com exatamente o mesmo nome, retornar os dados do usuário
# senão retornar falha
@router.get("/usuario/nome")
async def retornar_usuario_com_nome(nome: str):
    if UserValidation.valid_name(nome):
        return User.get_user_by_name(nome)
    return FALHA


# Se o id do usuário existir, deletar o usuário e retornar OK
# senão retornar falha
# ao deletar o usuário, deletar também endereços e carrinhos vinculados a ele
@router.delete("/usuario/")
async def deletar_usuario(id: int):
    if UserValidation.valid_id(id):
        User.delete_user(id)
        return OK
    return FALHA


# Se não existir usuário com o id_usuario retornar falha, 
# senão retornar uma lista de todos os endereços vinculados ao usuário
# caso o usuário não possua nenhum endereço vinculado a ele, retornar 
# uma lista vazia
### Estudar sobre Path Params (https://fastapi.tiangolo.com/tutorial/path-params/)
@router.get("/usuario/{id_usuario}/enderecos/")
async def retornar_enderecos_do_usuario(id_usuario: int):
    if UserValidation.valid_id(id_usuario):
        return Adress.get_adresses(id_usuario)
    return FALHA


# Retornar todos os emails que possuem o mesmo domínio
# (domínio do email é tudo que vêm depois do @)
# senão retornar falha
@router.get("/usuarios/emails/")
async def retornar_emails(dominio: str):
    if User.get_emails_by_domain(dominio):
        return {'emails': User.get_emails_by_domain(dominio)}
    return FALHA

# Se não existir endereço com o id_endereco retornar falha, 
# senão deleta endereço correspondente ao id_endereco e retornar OK
# (lembrar de desvincular o endereço ao usuário)
@router.delete("/usuario/{id_usuario}/endereco/{id_endereco}")
async def deletar_endereco(id_usuario: int, id_endereco: int):
    if AdressValidation.valid_to_delete(id_usuario, id_endereco):
        Adress.delete_adress(id_usuario, id_endereco)
        return OK
    return FALHA
