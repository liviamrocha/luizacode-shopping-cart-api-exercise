from app.schemas.adress import ListaDeEnderecosDoUsuario

# from pydantic import BaseModel
# from typing import List

# class Usuario(BaseModel):
#     id: int
#     nome: str
#     email: str
#     senha: str

# class Endereco(BaseModel):
#     id: int
#     rua: str
#     cep: str
#     cidade: str
#     estado: str


# class ListaDeEnderecosDoUsuario(BaseModel):
#     usuario: Usuario
#     enderecos: List[Endereco] = []

class Adress:
    
    db_enderecos = {}

    @classmethod
    def get_adresses(cls, user_id):
        if user_id in cls.db_enderecos:
            return cls.db_enderecos[user_id]['enderecos']
        else:
            return []

    @classmethod
    def add_adress(cls, adress, user):
        registed_adress = cls.get_adresses(user['id'])

        if registed_adress:
            cls.db_enderecos[user['id']]['enderecos'].append(adress.dict())
        else:
            adresses_list = ListaDeEnderecosDoUsuario(
                usuario=user,
                enderecos=[adress]
            )
            Adress.db_enderecos[user['id']] = adresses_list.dict()

    @classmethod
    def delete_adress(cls, user_id, adress_id):
        adresses = cls.db_enderecos[user_id]['enderecos']
        cls.db_enderecos[user_id]['enderecos']= list(filter(lambda i: i['id'] != adress_id, adresses))

    @classmethod
    def delete_all_adress(cls, user_id):
        return cls.db_enderecos.pop(user_id)

class AdressValidation:

    @classmethod
    def valid_to_add(cls, user_id, adress_id):
        adresses = Adress.get_adresses(user_id)
        for adress in adresses:
            if adress['id'] == adress_id:
                return False
        return True 
        
    @classmethod
    def valid_to_delete(cls, user_id, adress_id):
        adresses = Adress.get_adresses(user_id)
        for adress in adresses:
            if adress['id'] == adress_id:
                return True
        return False 