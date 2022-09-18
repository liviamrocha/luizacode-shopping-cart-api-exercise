from schemas.adress import ListaDeEnderecosDoUsuario
from controllers.users import User

class Adress:
    
    db_enderecos = {}

    def get_adresses(self, user_id):
        for register in Adress.db_enderecos:
            if register.usuario.id == user_id:
                return register.enderecos

    def add_adress(self, adress, user_id):
        adresses_list = ListaDeEnderecosDoUsuario(
            usuario=User.get_user_by_id(user_id),
            enderecos=[adress]
        )
        Adress.db_enderecos[user_id] = adresses_list

    # def delete_adress(self, adress_id):
    #     Adress.db_enderecos()


    