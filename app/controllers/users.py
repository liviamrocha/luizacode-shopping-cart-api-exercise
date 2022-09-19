
from app.controllers.carts import Cart
from app.controllers.adresses import Adress

class User:

    db_usuarios = {}

    @classmethod
    def add_user(cls, user):
        cls.db_usuarios[user.id] = user.dict()

    @classmethod
    def get_user_by_id(cls, id):
        return cls.db_usuarios[id] if id in cls.db_usuarios else False

    @classmethod
    def get_user_by_name(cls, nome):
        for id, user in cls.db_usuarios.items():
            if nome == user['nome']:
                return cls.db_usuarios[id] 
        return False

    @classmethod
    def delete_user(cls, id):
        cls.db_usuarios.pop(id)
        if Adress.get_adresses(id):
            Adress.delete_all_adress(id)
        elif Cart.get_cart(id):
            Cart.remove_cart(id)
    
    @classmethod
    def get_user_adresses(cls, id, db_enderecos):
        for registro in db_enderecos:
            if registro['usuario']['id'] == id:
                return registro['enderecos']

    @classmethod
    def get_emails_by_domain(cls, domain):
        emails = []
        for id, user in cls.db_usuarios.items():
            if domain == user['email'].split("@",1)[1]:
                emails.append(user['email'])
        return emails


class UserValidation:

    def __init__(self, user):
        self.user = user

    @classmethod
    def valid_id(self, user_id):
        return True if User.get_user_by_id(user_id) else False

    @classmethod
    def valid_name(self, user_name):
        return True if User.get_user_by_name(user_name) else False

    def valid_user(self):
        return (not UserValidation.valid_id(self.user.id)) and (self.valid_password()) and (self.valid_email())

    def valid_password(self):
        return True if len(self.user.senha) >= 3 else False

    def valid_email(self):
        return True if '@' in self.user.email else False

