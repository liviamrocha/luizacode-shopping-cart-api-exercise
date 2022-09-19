from pydantic import BaseModel
from typing import List


class Usuario(BaseModel):
    id: int
    nome: str
    email: str
    senha: str

class Endereco(BaseModel):
    id: int
    rua: str
    cep: str
    cidade: str
    estado: str

class ListaDeEnderecosDoUsuario(BaseModel):
    usuario: Usuario
    enderecos: List[Endereco] = []

class Produto(BaseModel):
    id: int
    nome: str
    descricao: str
    preco: float

class CarrinhoDeCompras(BaseModel):
    id_usuario: int
    produtos: List[Produto] = []
    preco_total: float
    quantidade_de_produtos: int