#Microatividade 2: Descrever a manipulação
#da estrutura de dados tupla em Python

primeira_tupla = 1 ,2 , 3, 4, "Olá, Tupla"  #tupla
print(type(primeira_tupla))
print("O conteúdo da tupla é:", primeira_tupla)

indice_4 = primeira_tupla.index(4)         #verificando um determinado elemento da lista
print("O indice do 4° elemento é:", indice_4)

contem_3 = 3 in primeira_tupla              #verificando se a tupla possui determinado elemento
print("A tupla contém o elemento 3?", contem_3)

contem_33 = 33 in primeira_tupla            #verificando se a tupla possui determinado elemento
print("A tupla contém o elemento 33?", contem_33)
