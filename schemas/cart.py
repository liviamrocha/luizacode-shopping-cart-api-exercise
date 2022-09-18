from pydantic import BaseModel
from typing import List
from .product import Produto


class CarrinhoDeCompras(BaseModel):
    id_usuario: int
    produtos: List[Produto] = []
    preco_total: float
    quantidade_de_produtos: int