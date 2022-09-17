from schemas.adresses import ListaDeEnderecosDoUsuario
from user import User

class Adress:
    
    def __init__(self):
        self.db_enderecos = {}

    def get_adresses(self, user_id):
        for register in self.db_enderecos:
            if register.usuario.id == user_id:
                return register.enderecos

    def add_adress(self, adress, user_id):
        adresses_list = ListaDeEnderecosDoUsuario(
            usuario=User.get_user_by_id(user_id),
            enderecos=[adress]
        )
        self.db_enderecos[user_id] = adresses_list

    # def delete_adress(self, adress_id):
    #     self.db_enderecos()


    