#Microatividade 3: Descrever a manipulação
#da estrutura de dados set em Python

set_inicial = {11, 12, 13, 14} #estrutura de dados
print(type(set_inicial))       #verificando o tipo
print("O conteúdo inicial do set é: ", set_inicial)

set_inicial.add(15)            #adicionando um novo elemento com o metodo .add()
print("O conteúdo do set com o elemento 15 adicionado:", set_inicial)

set_inicial.update([1,2,3,4,5]) #adicionando 5 novos elementos com o metodo .update()
print("O conteúdo do set com os novos elementos adicionados é:", set_inicial)

set_inicial.discard(13)  #removendo um elemento com o metodo .discard()
print("Conteúdo do set_inicial após remover 13:", set_inicial)

novo_set = {20, 21, 23, 1, 2}  #criando um novo set
print("Conteúdo do novo_set:", novo_set)

print("União entre set_inicial e novo_set:", set_inicial.union(novo_set))
#resultado da união entre set_inicial e novo_set

print("Interseção entre set_inicial e novo_set:", set_inicial.intersection(novo_set))
#resultado da interseção entre set_inicial e novo_set

print("Diferença entre set_inicial e novo_set:", set_inicial.difference(novo_set))
#resultado da diferença entre set_inicial e novo_set

print("Diferença simétrica entre set_inicial e novo_set:", set_inicial.symmetric_difference(novo_set))
#resultado da diferença simétrica entre set_inicial e novo_set