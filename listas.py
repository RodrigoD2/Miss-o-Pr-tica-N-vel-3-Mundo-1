#Microatividade 1: Descrever a manipulação
#da estrutura de dados lista em Python

lista_mesclada = [1, 2, 3, "Olá, Python", True, 12.6] #lista e seus argumentos
print(type(lista_mesclada))
print(lista_mesclada)

lista_mesclada.append("Lista alinhada") #acrecentando um item ao final da lista
print(lista_mesclada)

lista_mesclada.insert(4, 5)    #inserindo um item em uma determinada posição da lista
print(lista_mesclada)          #onde 4 é a posição e 5 é o item a ser inserido   

print(len(lista_mesclada))     #apresentando o tamanho da lista

lista_mesclada.remove(2)       #removenddo um intem de uma posição da lista
print(lista_mesclada)

print(lista_mesclada[1]) #verifica a posição de um item na lista
                         #onde o número [1] é a posição do item

#Cria uma nova lista apartir da anterior com os elementos até determinada posição
nova_lista_mesclada = lista_mesclada[:4]
print("Conteúdo da nova lista mesclada é:", nova_lista_mesclada)
