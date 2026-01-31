print('SISTEMA DE NOTAS')
print('...' * 10)
nome_aluno = input('Nome o aluno: ')
n1_port = float (input('Nota Portugues: '))
n2_mat = float (input('Nota Matematica: '))
n3_ing = float (input('Nota Ingles: '))

media = (n1_port+ n2_mat + n3_ing)/3

print('Situação do aluno: ')

aprovado = media > 7
reprovado = media < 5
recuperação = media >=5 and media <7
print('Aprovado? - ', aprovado)
print('Reprovado? - ', reprovado)
print('recuperação? - ', recuperação)
