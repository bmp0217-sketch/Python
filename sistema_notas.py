
#imprime numeros de 0 a 100
i = 0
while i <= 1000:
    print(i)
    i+=1

#lista para amarzenar os nomes
nomes = []
#contador para controlar o loop
i=0

print('digite o nome de 10 pessoas:')

#loop para cadastrar 10 nomes
while i <10:
    nome = input(f'nome {i+1}:')
    nomes.append(nome)
    i+=1
print('nome cadastrado:', nomes)
i=0
#loop para mostrar os nomes
while i <(nomes): 
    print(f'{i+1}. {nomes[i]}')
    i+=1