while True:
    print ('\n**Cadastro de paciente**')
    nome = input('nome: ')
    email = input('email:')
    idade = int(input('idade: '))
    peso = float(input('peso (kg): '))
    altura = float(input('altura(m): '))

    imc = peso / (altura ** 2)

    if imc <18.5:
        classificação = 'Abaixo do peso'
    elif imc <25:
        classificação = 'peso normal'
    elif imc <30:
        classificação = 'sobrepeso'
    elif imc <35:
        classificação = 'obesidade grau I'
    elif imc <40:
        classificação = 'obesidade grau II'
    else:
        classificação = 'obesidade grau III'

#amarzena os dados em um dicionario

paciente = {
    'Nome': nome,
    'e-mail': email,
    'peso (kg)' : peso,
    'altura (m)' : altura,
    'IMC': round (imc,2),
    'classificação' : classificação
}

#adiciona o paciente à lista
pacientes.append(paciente) #agora paciente esta declarado


continuar = input("Deseja continuar? (s/n):")
if continuar.lower() != 's':
    break

for i, paciente in enumerate(pacientes): 
    print(f'/n **paciente {i+1}**')
    for campo, valor in paciente.items():
        print(f'{campo}: {valor}')

#update

def editar():
    seleção = tree.selection()
    if selecao:
        user_id = tree.item(selecao)['values'][0]
        novo_nome = entry_nome.get()
        novo_email = entry_email.get()

        if novo_nome and novo_email:
            conn = conectar()
            c = conn.cursor()
            messagebox.showinfo('Sucesso', 'DADOS ATUALIZADOS')
            mostrar_usuario()
        else:
            menssagebox.showerror('erro', 'preencha todos os campos!')
            mostrar_usurio()
    else:
        messagebox.showerror('erro', 'selecione um usuario para editar')

#função axiliar para conectar ao banco de dados
def conectar():
    return sqlite3.connect('seu_banco_de_dados.db')

import tkinter as tk 
from tkinter import messagebox

#função para inserir um novo usuario
def inserir_usuario():
    nome = entry_nome.get()
    email = entry_email.get()
    cpf = entry_cpf.get()

    if nome and email and cpf:
        messagebox.showinfo('sucesso','usuario inserido com sucesso!')
        mostrar_usuario()
    else:
        messagebox.showwarning('Aviso', 'Preencha todos os campos!')

    

