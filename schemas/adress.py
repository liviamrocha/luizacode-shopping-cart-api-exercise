from pydantic import BaseModel
from typing import List
from .user import Usuario


class Endereco(BaseModel):
    rua: str
    cep: str
    cidade: str
    estado: str


class ListaDeEnderecosDoUsuario(BaseModel):
    usuario: Usuario
    enderecos: List[Endereco] = []