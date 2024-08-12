#Microatividade 5: Descrever a atualização
#de dados em um dicionário


dicionario_pessoas = {           #dicionário
    1: {'nome': 'Maria', 'idade': 26, 'nacionalidade': 'brasileira'}
}

novos_elementos = {                #novos elementos adionados
    2: {'nome': 'João', 'idade': 30, 'nacionalidade': 'portuguesa'},
    3: {'nome': 'Ana', 'idade': 22, 'nacionalidade': 'espanhola'}
}

dicionario_pessoas.update(novos_elementos)       #adicionando novos elementos ao dicionário
print("Dicionário de pessoas atualizado:", dicionario_pessoas)

novo_dicionario_pessoas = dicionario_pessoas.copy()   #criando uma cópia do dicionário
print("Novo dicionário de pessoas:", novo_dicionario_pessoas)

elemento_removido = dicionario_pessoas.pop(2)     #removendo elemento/pessoas
print("Conteúdo do primeiro dicionário após remover o elemento:", dicionario_pessoas)

print("Elemento removido:", elemento_removido)   #removendo o ultimo elemento do primeiro dicionário
elemento_removido = dicionario_pessoas.popitem()

print("Conteúdo do primeiro dicionário após remover o último elemento:", dicionario_pessoas)


dicionario_pessoas.clear()           #removendo todos os elementos dos dois dicionários
novo_dicionario_pessoas.clear()


novo_dicionario = dict.fromkeys(['a', 'b', 'c'], 0) #definindo o novo dicionário
print("Conteúdo do novo dicionário (items):", novo_dicionario.items())


print("Chaves do novo dicionário:", novo_dicionario.keys())
#imprenção das chaves do dicionário

print("Valores do novo dicionário:", novo_dicionario.values())
#imprenção dos valores do dicionário
