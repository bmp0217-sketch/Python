#crie um numero aleatorio de 5,10


import random

numero_aleatorio = random.randint(5,10)
print('numero aletório ente 5 e 10:', numero_aleatorio)

#crie 3 numero aleatórios


import random 
numeros = [random.randint(1,100) for _ in range(3)]
print ('tres numeros aleatórios')


#crie um numero aleatorio entre 10 a 30 utilize o range ()
import random
numero=random.choice(range(10,30))

print ('numero aleatorio entre 10 e 30:'[numero_aleatorio])

#contagem regressiva simples


for i in range (10,0,-1):
    print(i)
print ('Fogo!')

#Soma de numeros pares

numero = int(input( 'Digite um numero inteiro positivo: '))
resultado = soma_pares (numero)
print(f'A soma dos números pares de 2 até {numero} é: {resultado}')


