import tkinter as tk


root = tk.Tk()
root.title('IMC')
root.geometry('500x500')
root.iconbitmap('m2.png')

tk.Label(root,text= 'Digite o peso e a altura para ver o IMC', font=('arial',15)).pack(pady=20)

frm = tk.Frame(root)
frm.pack(pady=20)

input_peso = tk.Entry(root)
input_peso.pack(pady=10)


input_altura = tk.Entry(frm)
input_altura.pack(pady=20)
root.mainloop()

tk.Label(root,text= 'IMC', font=('arial',15)).pack(pady=20)