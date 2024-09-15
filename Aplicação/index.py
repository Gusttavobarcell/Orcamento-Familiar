# teste para ver se a biblioteca Tkinter está funcionando
import tkinter as tk

def salvar():
    n = nome.get()
    f = fone.get()
    print("Nome: " + n)
    print("Telefone: " + f)

win = tk.Tk()

win.title("Agenda")
win.geometry("300x300")
win.resizable(False, False)  # Impede que a janela seja redimensionada


lb1 = tk.Label(text = "Nome: ", background= "#dde", foreground = "#009")
lb1.place(x = 10,y = 10, width= 100, height= 20)

nome = tk.Entry()
nome.place(x = 10,y = 30, width= 200, height= 20)

lb2 = tk.Label(text = "telefone: ", background= "#dde", foreground = "#009")
lb2.place(x = 10,y = 60, width= 100, height= 20)

fone = tk.Entry()
fone.place(x = 10, y = 80, width= 200, height= 20)

bt1 = tk.Button(text= "Salvar", command=salvar)
bt1.place(x=10, y = 270, width= 100, height= 20)

tk.mainloop()



