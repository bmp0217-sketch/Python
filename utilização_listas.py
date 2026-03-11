carrinho = []
valores = []

print('E-COMMERCE Z')
print('SEJAM BEM VINDOS!')

produtos =  ['','jeep','ferrari','mercedez']
valores_prod = [0,50000.0,200000.0,500000.0]

produto_1 = int(input(f'''
                     
                      ESCOLHA UM PRODUTO:
                      1 - {produtos[1]} R$ - {valores_prod[1]}
                      2 - {produtos[2]} R$ - {valores_prod[2]}
                      3 - {produtos[3]} R$ - {valores_prod[3]}
                      ->  '''))

produto_2 = int(input(f'''
                     
                      ESCOLHA UM PRODUTO:
                      1 - {produtos[1]} R$ - {valores_prod[1]}
                      2 - {produtos[2]} R$ - {valores_prod[2]}
                      3 - {produtos[3]} R$ - {valores_prod[3]}
                      ->  '''))

carrinho.append(produtos[produto_1])
valores.append(valores_prod[produto_1])

print('VOCÊ ADICIONOU AO CARRINHO', carrinho)
print('R$', sum(valores))


carrinho.append(produtos[produto_2])
valores.append(valores_prod[produto_2])

print('VOCÊ ADICIONOU AO CARRINHO', carrinho)
print('R$', sum(valores))


formas_pag  = ['pix', 'cc', 'cd']

escolha = input(f'Escolha forma de pagamento, {formas_pag}')

print('sua forma de pagamento é ', escolha)
print('obrigada volte sempre!')
