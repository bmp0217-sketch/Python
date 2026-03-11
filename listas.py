# introdução a listas em python


v  =  10
# mista
lista_python =  [1,2,3,4,5,6, 10, 'texto', False, 5.2]

# inteiros
lista_inteiros  =  [4,2,3,6,5,0,1]


# decimal
lista_decimal =  [1.6,2.,3.]

# textos
lista_texto = ['teste', 'teste2', '250'  ]


# boleana
lista_boleana = [False, True, False]



# range / list

lista  =  [1,2,3,4,5,6]
print(lista)

l = list(range(1))
print(l)


# METODOS DA LISTA 



#       -4-3-2-1
lista = [10,1,2,3]
#        0 1 2 3
# acessar os indices

#  -----------------------------------------

# Métodos das listas:

print(lista[-1])

lista[-1] = 100

print(lista)


# métodos

lista_vazia = []
print(lista_vazia)


# inserir valores
# inserir apenas 1  dado
lista_vazia.append(200)
print(lista_vazia)

# inseir mais dados
lista_vazia.extend((10,20,30,60,50,40))
print(lista_vazia)

# insert vai inserir numa posição especifica
lista_vazia.insert(0,30)
print(lista_vazia)

lista_vazia+=(5,6,9,20,8,6,9,100)
print(lista_vazia)



# deletar valores

# remove  -  aplicar o valor que esta visualizando
lista_vazia.remove(200)
print(lista_vazia)

# del
del lista_vazia[0]
print(lista_vazia)

# pop / pop(indice)

lista_vazia.pop()
print('pop', lista_vazia)

lista_vazia.pop(0)
print(lista_vazia)


# verifica dado da lista
print('tamanho', len(lista_vazia))

# maior e menor
print('maior', max(lista_vazia))
print('menor', min(lista_vazia))


# reverse reverter sem ordenar


lista_vazia.reverse()
print(lista_vazia)

# ordenar a lista  -  organizar

lista_vazia.sort(reverse=True)
print(lista_vazia)

# x  =  sorted(lista_vazia)
# print(x)

# dir

# print(dir(lista_vazia))

# 'clear',

copia   = lista_vazia.copy()
print(copia)

# index -  indice

indice   =  lista_vazia.index(60)
print(indice)

# contar quantidade de valor

print(lista_vazia.count(20))


# limpar clear

lista_vazia.clear()
print(lista_vazia)



     # -3       -2        -1 (acessar)
L =  ['kaique','maria','lucas']
     #    0            1            2


print(L.index('maria'))