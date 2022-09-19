from shopping_cart.schemas.product import *
from shopping_cart.repository.products import *
from fastapi import APIRouter

router = APIRouter()

OK = "OK"
FALHA = "FALHA"

@router.get("/produto/")
async def retornar_todos_produtos():
    return Product.get_all_products()


# Se tiver outro produto com o mesmo ID retornar falha, 
# senão cria um produto e retornar OK
@router.post("/produto/")
async def criar_produto(produto: Produto):
    if not ProductValidation.valid_product(produto.id):
        Product.add_product(produto)
        return OK
    return FALHA


# Se não existir produto com o id_produto retornar falha, 
# senão deleta produto correspondente ao id_produto e retornar OK
# (lembrar de desvincular o produto dos carrinhos do usuário)
@router.delete("/produto/{id_produto}/")
async def deletar_produto(id_produto: int):
    if ProductValidation.valid_product(id_produto):
        Product.remove_product(id_produto)
        return OK
    return FALHA