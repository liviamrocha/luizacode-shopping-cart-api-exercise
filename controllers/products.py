class Product:

    db_produtos = {}

    @classmethod
    def get_product(cls, id):
        return cls.db_produtos[id] if id in cls.db_produtos else False

    @classmethod
    def add_product(cls, product):
        cls.db_produtos[product.id] = product.dict()

    @classmethod
    def remove_product(cls, product_id):
        cls.db_produtos.pop(product_id)

    @classmethod
    def add_to_cart(cls, product_id, user_id, db_carrinho):
        cls.db_carrinho[user_id] = cls.get_product(product_id)
        return db_carrinho

class ProductValidation:

    @classmethod
    def valid_product(cls, id):
        print(Product.get_product(id))
        return True if Product.get_product(id) else False
    