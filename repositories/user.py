
class User:

    def __innit__(self):
        self.db_usuarios = {}

    def add_user(self, user):
        self.db_usuarios[user.id] = user

    def get_user_by_id(self, id):
        return self.db_usuarios[id]

    def get_user_by_name(self, nome):
        for id, user in self.db_usuarios.items():
            if nome == user['nome']:
                return self.db_usuarios[id] 

    def delete_user(self, id):
        return self.db_usuarios.pop(id)

    def get_user_adresses(self, id, db_enderecos):
        for registro in db_enderecos:
            if registro['usuario']['id'] == id:
                return registro['enderecos']

    def get_emails_by_domain(self, domain):
        emails = []
        for id, user in self.db_usuarios.items():
            if domain == user['email'].split("@",1)[1]:
                emails.append(user['email'])
        return emails


class UserValidation:
    pass