import tkinter as tk
from tkinter import messagebox

# Listas para armazenar receitas e despesas
Nome_receita = []  
Nome_despesa  = []
valor_receita = []
valor_despesa = []
despesa_total = 0 
novosaldo = 0

def adicionar_receita():
    global valor_receita
    receita_nome = entrada_nomer.get().strip()
    receita_valor = entrada_valor.get().strip()

    if not receita_nome or not receita_valor:
        messagebox.showwarning("Atenção", "Insira o valor e o nome da Receita!!!")
        return
    try:
        receita_valor = float(receita_valor)  
    except ValueError:
        messagebox.showerror("Erro", "Adicione um valor válido")
        return

    valor_receita.append(receita_valor)
    Nome_receita.append(receita_nome)
    entrada_nomer.delete(0, tk.END) 
    entrada_valor.delete(0, tk.END)
    messagebox.showinfo("Sucesso", "Receita adicionada")
    print("Receitas: ", Nome_receita, valor_receita)

    result()

def adicionar_despesa():
    global valor_despesa
    despesa_nome = entrada_nomer2.get().strip()
    despesa_valor = entrada_valor2.get().strip()

    if not despesa_nome or not despesa_valor:
        messagebox.showwarning("Atenção", "Insira o valor e o nome da Despesa!!!")
        return
    try:
        despesa_valor = float(despesa_valor)  
    except ValueError:
        messagebox.showerror("Erro", "Adicione um valor válido")
        return

    valor_despesa.append(despesa_valor)
    Nome_despesa.append(despesa_nome)
    entrada_nomer2.delete(0, tk.END) 
    entrada_valor2.delete(0, tk.END)
    messagebox.showinfo("Sucesso", "Despesa adicionada")
    print("Despesas: ", Nome_despesa, valor_despesa)

    result()

def result(): # função para ssomar todos os valores da despesa quanto as receitas
    global novosaldo
    global despesa_total

    total_receita = sum(valor_receita)
    despesa_total = sum(valor_despesa)
    novosaldo = total_receita - despesa_total

    label3.config(text=f"Saldo é de: R${novosaldo:.2f}")

def mostrar_extrato(): #função para mostrar um extrato de todos os valores adicionados 
    janelaex_window = tk.Toplevel(janela)
    janelaex_window.title("Extrato")
    janelaex_window.geometry("400x400")
    janelaex_window.resizable(False, True)
    janelaex_window.configure(background="#1A434E")

    texto = tk.Text(janelaex_window, wrap='word',bg="#1A434E", fg="white")
    texto.pack(expand=True, fill='both')

    # cores distintas para a receita e a despesa
    texto.tag_configure("receita", foreground="white", font=("Arial", 12, "bold"))
    texto.tag_configure("despesa", foreground="red", font=("Arial", 12, "bold"))

    # adicionando as receitas por nome e o valor
    if Nome_receita:
        texto.insert(tk.END, "Receitas:\n", "receita")
        for nome, valor in zip(Nome_receita, valor_receita):
            texto.insert(tk.END, f"  {nome}: R${valor:.2f}\n", "receita")
        texto.insert(tk.END, "\n")
    else:
        texto.insert(tk.END, "Nenhuma receita adicionada.\n\n", "receita")

    # Adicionando as despesas pelo nome e o valor 
    if Nome_despesa:
        texto.insert(tk.END, "Despesas:\n", "despesa")
        for nome, valor in zip(Nome_despesa, valor_despesa):
            texto.insert(tk.END, f"  {nome}: R${valor:.2f}\n", "despesa")
    else:
        texto.insert(tk.END, "Nenhuma despesa adicionada.\n", "despesa")

    # colocando o texto para ser leitura ( não pode edita)
    texto.config(state='disabled')

def relat():
    relatorio_formatado = ""
    despesas_acima_300 = []
    despesas_maiores_saldo = []

    for nome, valor in zip(Nome_despesa, valor_despesa):
        if valor >= 300:
            despesas_acima_300.append((nome, valor))
        if valor > novosaldo:
            despesas_maiores_saldo.append((nome, valor))

    if despesa_total > sum(valor_receita):
        relatorio_formatado += "Suas despesas estão maiores que a sua receita!\n"


    if despesas_acima_300:
        relatorio_formatado += "Despesas acima de R$300! Tente economizar na área:\n"
        for nome, valor in despesas_acima_300:
            relatorio_formatado += f"  {nome}: R${valor:.2f}\n"


    if despesas_maiores_saldo:
        relatorio_formatado += "Suas despesas estão maiores que o saldo atual!\n"
        for nome, valor in despesas_maiores_saldo:
            relatorio_formatado += f"  {nome}: R$-{valor:.2f}\n"

    if relatorio_formatado:
        messagebox.showinfo("Relatório", relatorio_formatado)
    else:
        messagebox.showinfo("Relatório", "Nenhum problema relacionado as suas despesas foi identificado.")

# Configuração da tela principal
janela = tk.Tk()
janela.title("Orçamento Familiar")
janela.geometry("750x320")
janela.configure(background="#1A434E")
# janela.iconbitmap("assents\ygona.ico")
janela.resizable(False, False)


# style para os botões na tela principal
style_botão_receita = {
     "bg": "#8EBEF1",  
    "fg": "white",
    "width": 15,
    "activebackground": "#475F79",
    "activeforeground": "white",
}
style_botão_despesa = {
     "bg": "#DFB33A",
    "fg": "white",
    "width": 15,
    "activebackground": "#B09A5D",
    "activeforeground": "white",
}

style_botão_extrato = {
     "bg": "#2A5F23",  
    "fg": "white",
    "width": 15,
    "activebackground": "#0B1809",
    "activeforeground": "white",
}

style_botão_relatorio = {
     "bg": "#EF5976", 
    "fg": "white",
    "width": 15,
    "activebackground": "#782D3B",
    "activeforeground": "white",
}

# Labels para Receita
label1 = tk.Label(janela, text="Nome da Receita", bg="#1A434E", fg="white",font=("Arial", 13))
label1.grid(row=0, column=1, padx=(5, 5), pady=(10,0))

linha = tk.Frame(janela, height=3, bg="#8EBEF1")  # Cor da linha
linha.grid(row=0, column=1, sticky="ew",padx=(60, 60), pady=(40,0))  


label2 = tk.Label(janela, text="Valor da Receita", bg="#1A434E", fg="white",font=("Arial", 13))
label2.grid(row=0, column=2, padx=(5, 5), pady=(10,0))

linha = tk.Frame(janela, height=3, bg="#8EBEF1") 
linha.grid(row=0, column=2, sticky="ew",padx=(60, 50), pady=(40,0))  


# Labels para Despesa
label6 = tk.Label(janela, text="Nome da Despesa", bg="#1A434E", fg="white",font=("Arial", 13))
label6.grid(row=2, column=1, padx=(10, 5), pady=(5,0))

linha = tk.Frame(janela, height=3, bg="#DFB33A")  # Cor da linha
linha.grid(row=2, column=1, sticky="ew",padx=(60, 50), pady=(40,0)) 


label7 = tk.Label(janela, text="Valor da Despesa", bg="#1A434E", fg="white",font=("Arial", 13))
label7.grid(row=2, column=2, padx=(5, 5), pady=(5,0))

linha = tk.Frame(janela, height=3, bg="#DFB33A")  # Cor da linha
linha.grid(row=2, column=2, sticky="ew",padx=(60,50), pady=(40,0))


# Label do saldo 
label3 = tk.Label(janela, text="Saldo: R$0.00", bg="#1A434E", fg="white",font=("Arial", 13))
label3.grid(row=6, column=1, padx=5, pady=(50,0))


# Entradas para armaznar dados da Receita
entrada_nomer = tk.Entry(janela,font=("Arial", 13))
entrada_nomer.grid(row=1, column=1, padx=(60, 5), pady=5)
entrada_valor = tk.Entry(janela,font=("Arial", 13))
entrada_valor.grid(row=1, column=2, padx=(60, 5), pady=5)

# Entradas para as Despesas
entrada_nomer2 = tk.Entry(janela,font=("Arial", 13))
entrada_nomer2.grid(row=3, column=1, padx=(60, 5), pady=5)
entrada_valor2 = tk.Entry(janela,font=("Arial", 13))
entrada_valor2.grid(row=3, column=2, padx=(60, 5), pady=5)

# Botões para adicionar Receita e Despesa
botao_receita = tk.Button(janela, text="Adicionar Receita", command=adicionar_receita,**style_botão_receita ,font=("Arial", 10))
botao_receita.grid(row=1, column=3, padx=(30, 5), pady=5)

botao_despesa = tk.Button(janela, text="Adicionar Despesa", command=adicionar_despesa,**style_botão_despesa, font=("Arial", 10))
botao_despesa.grid(row=3, column=3, padx=(30, 5), pady=5)

# Botão para mostrar o Extrato
botao_extrato = tk.Button(janela, text="Ver Extrato", command=mostrar_extrato,**style_botão_extrato)
botao_extrato.grid(row=7, column=1, padx=0, pady=5)

# Botão para gerar o Relatório
botao_relatorio = tk.Button(janela, text="Gerar Relatório", command=relat,**style_botão_relatorio)
botao_relatorio.grid(row=8, column=3, padx=(45, 5), pady=5)



janela.mainloop()

