class Product:

    def __init__(self):
        self.db_produtos = {}

    def get_product(self, product_id):
        return self.db_produtos[product_id]

    def add_product(self, product):
        self.db_produtos[product.id] = product

    def remove_product(self, product_id):
        self.db_produtos.pop(product_id)

    def add_to_cart(self, product_id, user_id, db_carrinho):
        self.db_carrinho[user_id] = self.get_product(product_id)
        return db_carrinho

class ProductValidation:
    pass