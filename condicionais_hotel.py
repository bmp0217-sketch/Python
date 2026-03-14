dados = {
'nomes':[],
'idades':[],
'quartos':['', "Simples", "Duplo" , "Luxo"],
'valores':[0 , 100.0,150.0,250.0],
'quartos_escolhidos':[],
'valores_a_pagar':[],
'dias':[]
}

quantidade_de_pessoas = int(input('Quantidade de Pessoas:'))

if quantidade_de_pessoas == 1:
    dados['nomes'].append(input('Digite  o nome: '))
    dados['idades'].append(input('Digite  a Idade: '))

# logica
    print('escolha um quarto:', dados['quartos'])

    print('escolha o quarto - 1 - 2 - 3')

    escolha  =  int(input('Escolha o seu quarto -> '))

    dados['quartos_escolhidos'].append(dados['quartos'][escolha])
    dados['valores_a_pagar'].append(dados['valores'][escolha])

    print(dados['quartos_escolhidos'], 'R$', dados['valores_a_pagar'])
   
    q_dias  =  int(input('Quantidade de dias -> '))
    total   =  dados['valores_a_pagar'] * q_dias
   
    print('Total R$ ', sum(total))
    pagar = input('Digite a forma de pagamento: ')
    print('Forma de pagamento', pagar)



# elif quantidade_de_pessoas == 2:
#     dados['nomes'].append(input('Digite  o nome: '))
#     dados['idades'].append(input('Digite  a Idade: '))    
#     dados['nomes'].append(input('Digite  o nome: '))
#     dados['idades'].append(input('Digite  a Idade: '))

#     # logica

# elif quantidade_de_pessoas == 3:
#     dados['nomes'].append(input('Digite  o nome: '))
#     dados['idades'].append(input('Digite  a Idade: '))    
#     dados['nomes'].append(input('Digite  o nome: '))
#     dados['idades'].append(input('Digite  a Idade: '))    
#     dados['nomes'].append(input('Digite  o nome: '))
#     dados['idades'].append(input('Digite  a Idade: '))    


#     # logica

# else:
#     print('Digite algo válido... ')