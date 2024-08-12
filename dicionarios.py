#Microatividade 4: Descrever a criação da
#estrutura de dados dicionário em Python

#estrutura de dados do tipo dicionário
meu_dicionario = {
    1: "Python",
    2: "Java",
    3: "PHP"
}

#imprenção do conteúdo do dicionário
print("Conteúdo do meu_dicionario:", meu_dicionario)

#imprenção do tipo de dados do dicionário utilizando o método “type”
print("Tipo de dados de meu_dicionario:", type(meu_dicionario))

#utilizando o método “get”, imprimir o valor da chave “linguagem”
print("Valor da chave 'linguagem' para o código 1:", meu_dicionario.get(1))
print("Valor da chave 'linguagem' para o código 2:", meu_dicionario.get(2))
print("Valor da chave 'linguagem' para o código 3:", meu_dicionario.get(3))

#imprenção do tamanho do dicionário
print("Tamanho de meu_dicionario:", len(meu_dicionario))

#utilizando o método “dict” criar um novo dicionário, aninhado,
#chamado “dicionario_frutas”
dicionario_frutas = {
    1: {"nome": "limão", "tipo": "ácida"},
    2: {"nome": "laranja", "tipo": "ácida"},
    3: {"nome": "manga", "tipo": "semiácida"},
    4: {"nome": "maçã", "tipo": "semiácida"},
    5: {"nome": "banana", "tipo": "doce"},
    6: {"nome": "mamão", "tipo": "doce"}
}

#imprenção do valor das chaves “nome” e “tipo” da chave 1
print("Valores da chave 1 em dicionario_frutas:", dicionario_frutas[1])

#imprenção do valor das chaves “nome” e “tipo” da chave 2
print("Valores da chave 2 em dicionario_frutas:", dicionario_frutas[2])

#utilizando o método for para iterar no dicionário “dicionario_frutas” e
#imprimir os valores de todas as chaves “nome” e “tipo”
for chave, valor in dicionario_frutas.items():
    print(f"Valores da chave {chave} em dicionario_frutas: nome = {valor['nome']}, tipo = {valor['tipo']}")
