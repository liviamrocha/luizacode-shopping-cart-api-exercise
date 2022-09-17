from functools import reduce

class Cart:

    def __init__(self):
        self.db_carrinho = {}

    def add_cart(self, user_id, cart):
        self.db_carrinho[user_id] = cart

    def remove_cart(self, user_id):
        return self.db_carrinho.pop(user_id)

    def get_cart(self, user_id):
        return self.db_carrinho[user_id]

    def get_cart_total(self, user_id):
        get_total = lambda x: x.preco * x.quantidade_de_produtos
        return reduce(get_total, self.db_carrinho[user_id].values())

class CartValidation:
    pass