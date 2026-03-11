# metodo dinamico

dados_escola  = {}

dados_escola['nomes_alunos'] = [input('nome: '), input('nome: '), input('nome:')]
dados_escola['notas'] = [[5,6,5],[10,10,10],[9,6,0]]  

print(dados_escola)
print('sistema de média: ')

aluno_1 = dados_escola['nomes_alunos'][0]
aluno_2 = dados_escola['nomes_alunos'][1]
aluno_3 = dados_escola['nomes_alunos'][2]

media_1 =  sum(dados_escola['notas'][0])/len(dados_escola['notas'][0])
media_2 =  sum(dados_escola['notas'][1])/len(dados_escola['notas'][1])
media_3 =  sum(dados_escola['notas'][2])/len(dados_escola['notas'][2])

print(f'''

MÉDIA:
     
ALUNO {aluno_1 } MEDIA - {media_1}
ALUNO {aluno_2 } MEDIA - {media_2}
ALUNO {aluno_3 } MEDIA - {media_3}


''')



ecommerce = {

'livro':'antifragil',
'tablets':'dell',
'fones': 'apple'

}


ecommerce = {

'prod1 ':'livro',
'prod2':'tablets',
'prod3': 'fone'

}




ecommerce = {


'livros':{
    'ficção': ['antifragil', 'cisne negro', 'homo deus'],
    'romance':['a','b','c']
    },


'tablets':['dell', 'samsumg','positivo'],
'fones': ['apple', 'motorola', 'jbl']

}

print(ecommerce['livros']['romance'][2])