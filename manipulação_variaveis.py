# # print('Testes')

# print('Teste')
# print()
# print('teste2')


# 4  tipos de dados primitivos

# string -  dados do tipo texto -  "Texto"
# float  - dados do tipo decimals -   5.0
# bool  -  dados do tipo lógico  -  True / False
# int - dados do tipo inteiro  -  10  1  -2  0

# variáveis
# nome semântico, começar por letra, snake_case(palavra composta),
# Não começa por número, dados únicos
# estrutura de dados

nome = "Eloysa"
sobrenome = 'Lima'
idade = 25
endereco = 'Rua 20 nº 2'
peso = 65.5
solteira = False


print(nome,sobrenome)
print('Idade:\n', idade)
print('Peso: ', peso)
print('Endereço:', endereco)
print('Estado Civil solteiro:', solteira)

n1 = 10
n2  = 20

print(n1 + n2)

# input()

# nome  =  input('Nome: ')
# sobrenome =  input('Sobrenome: ')
# idade = input('Idade: ')
# endereco = input('Endereço: ')
# peso = input('Peso: ')
# solteira = input('Estado CiviL: ')



# Pemdas    03      01       02
# x  =  10 + 20 + (10*2) - 50 ** 2
# print(x)



# Sinais aritméticos

# print(10 + 1)
# print(10 - 1)
# print(10 * 1)
# print(10 / 1)
print(10 // 3) # int // int = int  |  dec // in = dec
print(10 % 3) # volta o resto da conta de divisão
print(10 ** 2) # potencia

# Sinais lógicos -  True / False

print(10 > 1) # True
print(10 < 1) # False
print('Teste:', 10 >= 1) # > ou = 1 | 1 or 0 - True
print(10 <= 1) # 0  0 = False
print(10 == 1) # 0 = false
print(10 != 1) # True

# pular linhas
print(nome)
print(sobrenome)

print()

print(f'{nome}\n{sobrenome}')

print(f'''
{nome}
{sobrenome}
''')