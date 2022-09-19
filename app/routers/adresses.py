# Se não existir usuário com o id_usuario retornar falha, 
# senão cria um endereço, vincula ao usuário e retornar OK
@app.post("/endereco/{id_usuario}/")
async def criar_endereco(endereco: Endereco, id_usuario: int):
    if id_usuario in db_usuarios:
        lista_enderecos = ListaDeEnderecosDoUsuario(usuario=db_usuarios[id_usuario])
        lista_enderecos.enderecos.append(endereco.dict())
        lista_enderecos = lista_enderecos.dict()
        db_end[lista_enderecos['usuario']['id']] = lista_enderecos['enderecos'].append(endereco)
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
