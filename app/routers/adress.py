from app.schemas.user import *
from app.schemas.adress import *
from app.controllers.users import *
from app.controllers.adresses import *

from fastapi import APIRouter

router = APIRouter()

OK = "OK"
FALHA = "FALHA"


# Se não existir usuário com o id_usuario retornar falha, 
# senão cria um endereço, vincula ao usuário e retornar OK
@router.post("/endereco/{id_usuario}/")
async def criar_endereco(endereco: Endereco, id_usuario: int):
    if UserValidation.valid_id(id_usuario) and AdressValidation.valid_to_add(id_usuario, endereco.id):
        usuario = User.get_user_by_id(id_usuario)
        Adress.add_adress(endereco, usuario)
        return OK
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