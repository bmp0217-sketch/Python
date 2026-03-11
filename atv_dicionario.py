# Crie um e-commerce com a estrutura de dicionários.
# Produtos:  Livros, tablets e fones de ouvido
# As ações:
# Comprar()
# Pagar()
# mostra o valor da compra


# e_commerce =  {
# 'Livros': 10.5,
# 'tablets':150.0,
# 'fones de ouvido':250
# }

# print('E-commerce x')
# print('Produtos: ', e_commerce)

# carrinho = []
# valores = []

# p1  =  input('Digite o produto: ')

# carrinho.append(p1)
# valores.append(e_commerce[p1])

# print('produto: ',carrinho,'R$',valores )

# --------------------------------------------------------------


ecommerce = {


1:['a','b','c'],
2: [10,20,30],
3:['a','b','c'],
4: [10,20,30],
5:['a','b','c'],
6: [10,20,30],



}

carrinho = []
valores = []

secao = input('Secão')
p1 = int(input('Id do produto'))

carrinho.append(ecommerce[secao][p1])
valores.append(ecommerce['Livros_valores'][p1])



# ---------------------------------------------



ecommerce ={

'Livros':{

'a':50,
'b':60

},
'tablets':{

'a':50,
'b':60

},

'fones de ouvido':
{
'a':50,
'b':60

}

}



carrinho = []
valores  = []

secao = input('Secão: ')
p1  =  input('Produto: ')


carrinho.append(p1)
valores.append(ecommerce[secao][p1])


print(carrinho)
print(valores)


# ---------------------------------------------


ecommerce ={

'marca a':
{
'modelo a': 100,
'modelo b':500,
'modelo c':400,
},

'marca b':{
'modelo a': 100,
'modelo b':500,
'modelo c':400,
},


'marca c':{
'modelo a': 100,
'modelo b':500,
'modelo c':400,
},



}


# ===============================



ecommerce ={

'marca a':['', 'modelo a', 100,'modelo b',500,'modelo c',400],

'marca b':['', 'modelo a', 100,'modelo b',500,'modelo c',400],

'marca c':['', 'modelo a', 100,'modelo b',500,'modelo c',400],


}


carrinho = []
valores = []

marca = input('Secão: ')
p1  =  input('Produto: ')

i = ecommerce[marca].index(p1)

carrinho.append(ecommerce[marca][i])

i   =  ecommerce[marca].index(p1)
valores.append(ecommerce[marca][i]+1)