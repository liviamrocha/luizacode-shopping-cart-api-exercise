from functools import reduce

class Cart:

    db_carrinho = {}

    def add_cart(self, user_id, cart):
        Cart.db_carrinho[user_id] = cart

    def remove_cart(self, user_id):
        return Cart.db_carrinho.pop(user_id)

    def get_cart(self, user_id):
        return Cart.db_carrinho[user_id]

    def get_cart_total(self, user_id):
        get_total = lambda x: x.preco * x.quantidade_de_produtos
        return reduce(get_total, Cart.db_carrinho[user_id].values())

class CartValidation(Cart):
    
    def __init__(self, user_id):
        super().__init__()
        self.user_id = user_id

    def cart_exist(self):
        return True if Cart.get_cart(self.user_id) else False
