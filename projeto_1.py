from fastapi import FastAPI, status, HTTPException
from typing import List
from pydantic import BaseModel
from schemas import adress, cart, product, user
from controllers import users, adresses, carts, products


app = FastAPI()

OK = "OK"
FALHA = "FALHA"


# Criar um usuário,
# se tiver outro usuário com o mesmo ID retornar falha, 
# se o email não tiver o @ retornar falha, 
# senha tem que ser maior ou igual a 3 caracteres, 
# senão retornar OK
@app.post("/usuario/")
async def criar_usuário(usuario: user.Usuario):
    if users.UserValidation(usuario).valid_user():
        users.User.add_user(usuario)
        return OK
    return FALHA


# Se o id do usuário existir, retornar os dados do usuário
# senão retornar falha
@app.get("/usuario/")
async def retornar_usuario(id: int):
    if users.UserValidation.valid_id(id):
        return users.User.get_user_by_id(id)
    return FALHA


# Se existir um usuário com exatamente o mesmo nome, retornar os dados do usuário
# senão retornar falha
@app.get("/usuario/nome")
async def retornar_usuario_com_nome(nome: str):
    if users.UserValidation.valid_name(nome):
        return users.User.get_user_by_name(nome)
    return FALHA


# Se o id do usuário existir, deletar o usuário e retornar OK
# senão retornar falha
# ao deletar o usuário, deletar também endereços e carrinhos vinculados a ele
@app.delete("/usuario/")
async def deletar_usuario(id: int):
    if users.UserValidation.valid_id(id):
        users.User.delete_user(id)
        return OK
    return FALHA


# Se não existir usuário com o id_usuario retornar falha, 
# senão retornar uma lista de todos os endereços vinculados ao usuário
# caso o usuário não possua nenhum endereço vinculado a ele, retornar 
# uma lista vazia
### Estudar sobre Path Params (https://fastapi.tiangolo.com/tutorial/path-params/)
@app.get("/usuario/{id_usuario}/endereços/")
async def retornar_enderecos_do_usuario(id_usuario: int):
    return FALHA


# Retornar todos os emails que possuem o mesmo domínio
# (domínio do email é tudo que vêm depois do @)
# senão retornar falha
@app.get("/usuarios/emails/")
async def retornar_emails(dominio: str):
    if users.User.get_emails_by_domain(dominio):
        return users.User.get_emails_by_domain(dominio)
    return FALHA


# Se não existir usuário com o id_usuario retornar falha, 
# senão cria um endereço, vincula ao usuário e retornar OK
@app.post("/endereco/{id_usuario}/")
async def criar_endereco(endereco: adress.Endereco, id_usuario: int):
    if id_usuario in db_usuarios:
        lista_enderecos = adress.ListaDeEnderecosDoUsuario(usuario=db_usuarios[id_usuario])
        lista_enderecos.enderecos.append(endereco.dict())
        lista_enderecos = lista_enderecos.dict()
        db_end[lista_enderecos['usuario']['id']] = lista_enderecos['enderecos'].append(endere)
        print(db_end)
        # db_end[lista_enderecos['usuario'][id_usuario]]
        # lista_enderecos = ListaDeEnderecosDoUsuario(
        #     usuario=,
        #     enderecos=endereco.dict()
        # )
        # db_end[lista_enderecos.usuario.id] = lista_enderecos.enderecos
        print(db_end)
    return FALHA


# Se não existir endereço com o id_endereco retornar falha, 
# senão deleta endereço correspondente ao id_endereco e retornar OK
# (lembrar de desvincular o endereço ao usuário)
@app.delete("/endereco/{id_endereco}/")
async def deletar_endereco(id_endereco: int):
    return OK


# Se tiver outro produto com o mesmo ID retornar falha, 
# senão cria um produto e retornar OK
@app.post("/produto/")
async def criar_produto(produto: product.Produto):
    if products.ProductValidation.valid_product(produto.id):
        return FALHA
    products.Product.add_product(produto)
    return OK


# Se não existir produto com o id_produto retornar falha, 
# senão deleta produto correspondente ao id_produto e retornar OK
# (lembrar de desvincular o produto dos carrinhos do usuário)
@app.delete("/produto/{id_produto}/")
async def deletar_produto(id_produto: int):
    if not products.ProductValidation.valid_product(id_produto):
        return FALHA
    products.Product.remove_product(id_produto)
    return OK

# Se não existir usuário com o id_usuario ou id_produto retornar falha, 
# se não existir um carrinho vinculado ao usuário, crie o carrinho
# e retornar OK
# senão adiciona produto ao carrinho e retornar OK
@app.post("/carrinho/{id_usuario}/{id_produto}/")
async def adicionar_carrinho(id_usuario: int, id_produto: int):
    return OK


# Se não existir carrinho com o id_usuario retornar falha, 
# senão retorna o carrinho de compras.
@app.get("/carrinho/{id_usuario}/")
async def retornar_carrinho(id_usuario: int):
    return cart.CarrinhoDeCompras


# Se não existir carrinho com o id_usuario retornar falha, 
# senão retorna o o número de itens e o valor total do carrinho de compras.
@app.get("/carrinho/{id_usuario}/")
async def retornar_total_carrinho(id_usuario: int):
    numero_itens, valor_total = 0
    return numero_itens, valor_total


# Se não existir usuário com o id_usuario retornar falha, 
# senão deleta o carrinho correspondente ao id_usuario e retornar OK
@app.delete("/carrinho/{id_usuario}/")
async def deletar_carrinho(id_usuario: int):
    return OK


@app.get("/")
async def bem_vinda():
    site = "Seja bem vinda"
    return site.replace('\n', '')