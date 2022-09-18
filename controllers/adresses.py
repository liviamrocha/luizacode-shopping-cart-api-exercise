from .users import User
from pydantic import BaseModel
from typing import List

class Usuario(BaseModel):
    id: int
    nome: str
    email: str
    senha: str

class Endereco(BaseModel):
    id: int
    rua: str
    cep: str
    cidade: str
    estado: str


class ListaDeEnderecosDoUsuario(BaseModel):
    usuario: Usuario
    enderecos: List[Endereco] = []

class Adress:
    
    db_enderecos = {}

    @classmethod
    def get_adresses(cls, user_id):
        if user_id in cls.db_enderecos:
            return cls.db_enderecos[user_id]['enderecos']
        else:
            return False

    @classmethod
    def add_adress(cls, adress, user_id):
        registed_adress = cls.get_adresses(user_id)

        if registed_adress:
            cls.db_enderecos[user_id]['enderecos'].append(adress.dict())
        else:
            adresses_list = ListaDeEnderecosDoUsuario(
                usuario=User.get_user_by_id(user_id),
                enderecos=[adress]
            )
            Adress.db_enderecos[user_id] = adresses_list.dict()

    @classmethod
    def delete_adress(cls, user_id, adress_id):
        adresses = cls.db_enderecos[user_id]['enderecos']
        cls.db_enderecos[user_id]['enderecos']= list(filter(lambda i: i['id'] != adress_id, adresses))

class AdressValidation:

    @classmethod
    def valid_adress(cls, user_id):
        return True if Adress.get_adresses(user_id) else False

