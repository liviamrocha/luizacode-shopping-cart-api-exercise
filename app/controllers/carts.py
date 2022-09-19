from functools import reduce
from app.schemas.cart import CarrinhoDeCompras

# from pydantic import BaseModel
# from typing import List

# class Usuario(BaseModel):
#     id: int
#     nome: str
#     email: str
#     senha: str
# class Produto(BaseModel):
#     id: int
#     nome: str
#     descricao: str
#     preco: float

# class CarrinhoDeCompras(BaseModel):
#     id_usuario: int
#     produtos: List[Produto] = []
#     preco_total: float
#     quantidade_de_produtos: int

class Cart:

    db_carrinho = {}

    @classmethod
    def add_cart(cls, user_id, product):
        registered_cart = cls.get_cart(user_id)

        if registered_cart:
            cls.db_carrinho[user_id]['produtos'].append(product)
            cls.db_carrinho[user_id]['preco_total'] += product['preco']
            cls.db_carrinho[user_id]['quantidade_de_produtos'] = len(cls.db_carrinho[user_id]['produtos'])
        else:
            cart = CarrinhoDeCompras(
                id_usuario=user_id, 
                produtos=[product],
                preco_total=product['preco'], 
                quantidade_de_produtos=1
            )
            
            Cart.db_carrinho[user_id] = cart.dict()

    @classmethod
    def remove_cart(cls, user_id):
        return Cart.db_carrinho.pop(user_id)

    @classmethod
    def remove_product(cls, product_id):
        for cart in cls.db_carrinho.values():
            cart['produtos'] = [i for i in cart['produtos'] if not (i['id'] == product_id)]
        cls.recalculate_total()
    
    @classmethod
    def get_cart(cls, user_id):
        return cls.db_carrinho[user_id] if user_id in cls.db_carrinho else False

    @classmethod
    def get_cart_total(cls, user_id):
        cart = cls.get_cart(user_id)
        get_item_total = lambda total, preco: total + preco['preco'] 
        return reduce(get_item_total, cart['produtos'], 0)

    @classmethod
    def get_cart_quantity(cls, user_id):
        cart = cls.get_cart(user_id)
        return len(cart['produtos'])

    @classmethod
    def get_product(cls, product_id):
        for cart in cls.db_carrinho.values():
            if not any(produto['id'] == product_id for produto in cart['produtos']):
                return False
            return True

    @classmethod
    def recalculate_total(cls):
        for user_id, cart in cls.db_carrinho.items():
            cart['quantidade_de_produtos'] = len(cart['produtos'])
            cart['preco_total'] = cls.get_cart_total(user_id)


class CartValidation(Cart):

    @classmethod
    def valid_cart(cls, user_id):
        return True if Cart.get_cart(user_id) else False

# if __name__ == '__main__':
#     user = user.Usuario(id=1, nome='livia', email='teste@gmail.com', senha='1234')
#     usuario = User()
#     usuario.add_user(user)

#     produto1 = product.Produto(id=1, nome='Sorvete', descricao='Doce gelado', preco=9.99)
#     produto2 = Produto(id=2, nome='Picolé', descricao='Doce gelado', preco=2)
#     product = Product()
#     product.add_product(produto1)
#     product.add_product(produto2)

#     cart = Cart()
#     cart.add_cart(1, 1)
#     cart.add_cart(1, 2)

#     print(cart.get_cart_quantity(1))
    