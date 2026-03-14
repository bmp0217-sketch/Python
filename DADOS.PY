dados_alunos  = {

'autenticacao':{
'senha':'123',
'login':'bea',
},
'media':[]

}

# [input('digite o nome do aluno')] = [float(input('nota1')), float(input('nota2'))]

for chances in range(3):
    print('ESCOLAR xxxxxx')
    senha  =  input('DIGITE SUA SENHA: ')
    if senha == dados_alunos['autenticacao']['senha']:
       
        print('cadastro das notas ... ')
       
        q = int(input('quantidade de alunos: '))

        for quantidade in range(q):
            nome = input('nome: ')
            dados_alunos[nome] = [float(input('nota 1')), float(input('nota 2')), float(input('nota 3'))]
            media  =  sum(dados_alunos[nome]) / len((dados_alunos[nome]))
            print('Media do aluno:',nome, '>>>>',  media)
        dados_alunos['media'].append(media)
        media_turma = sum(dados_alunos['media']) / len(dados_alunos['media'])  
        print('media da turma:' , media_turma )    
               
    else:
        print('Senha incorreta tente novamente...')            
           

else:
    print('Conta bloqueada ....')


input('digite enter para sair ....')