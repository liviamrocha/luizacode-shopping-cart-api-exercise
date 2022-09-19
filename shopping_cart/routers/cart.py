from shopping_cart.repository.users import *
from shopping_cart.repository.products import *
from shopping_cart.repository.carts import *
from fastapi import APIRouter

router = APIRouter()

OK = "OK"
FALHA = "FALHA"

# Se não existir usuário com o id_usuario ou id_produto retornar falha, 
# se não existir um carrinho vinculado ao usuário, crie o carrinho
# e retornar OK
# senão adiciona produto ao carrinho e retornar OK
@router.post("/carrinho/{id_usuario}/{id_produto}/")
async def adicionar_carrinho(id_usuario: int, id_produto: int):
    if UserValidation.valid_id(id_usuario) and ProductValidation.valid_product(id_produto):
        product = Product.get_product(id_produto)
        Cart.add_cart(id_usuario, product)
        return OK
    return FALHA


# Se não existir carrinho com o id_usuario retornar falha, 
# senão retorna o carrinho de compras.
@router.get("/carrinho/{id_usuario}/")
async def retornar_carrinho(id_usuario: int):
    if CartValidation.valid_cart(id_usuario):
        return Cart.get_cart(id_usuario)
    return FALHA


# Se não existir carrinho com o id_usuario retornar falha, 
# senão retorna o o número de itens e o valor total do carrinho de compras.
@router.get("/carrinho/total/{id_usuario}/")
async def retornar_total_carrinho(id_usuario: int):
    if CartValidation.valid_cart(id_usuario):
        numero_itens = Cart.get_cart_quantity(id_usuario)
        valor_total = Cart.get_cart_total(id_usuario)
        return {'quantidade_de_itens': numero_itens, 'total': round(valor_total, 2)}
    return FALHA


# Se não existir usuário com o id_usuario retornar falha, 
# senão deleta o carrinho correspondente ao id_usuario e retornar OK
@router.delete("/carrinho/{id_usuario}/")
async def deletar_carrinho(id_usuario: int):
    if CartValidation.valid_cart(id_usuario):
        Cart.remove_cart(id_usuario)
        return OK
    return FALHA