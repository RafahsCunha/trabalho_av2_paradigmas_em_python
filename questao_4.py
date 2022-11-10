# 4 - Utilizando a biblioteca gráfica Tkinter, o aluno deve construir uma interface que simule uma tela de
# login de usuário contendo o campo de login, senha e um botão de autenticação. (2,0 pontos).

from ast import Raise
from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox

# Cores -----------

co0 = "#f0f3f5"  # Preta / black
co1 = "#feffff"  # branca / white
co2 = "#3fb5a3"  # verde / green
co3 = "#38576b"  # valor / value
co4 = "#403d3d"   # letra / letters

# Janela
janela = Tk()
janela.title('')
janela.geometry('310x300')  # largura
janela.configure(background=co1)  # cor de fundo - branco
# o método resizable() permite que a janela raiz mude de tamalho ou não
janela.resizable(width=FALSE, height=FALSE)


# dividindo a janela
frame_cima = Frame(janela, width=310, height=50, bg=co1, relief='flat')
frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)


frame_baixo = Frame(janela, width=310, height=250, bg=co1, relief='flat')
frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)


# Configurando o frame de cima
label_nome = Label(frame_cima, text='Tela de Login',
                   anchor=NE, font=('Ivy 25'), bg=co1, fg=co4)
label_nome.place(x=5,y=5)


label_linha = Label(frame_cima, text='', width=275, anchor=NW, font=('Ivy 1'), bg=co2, fg=co4)
label_linha.place(x=10,y=45)


# Configurando o frame baixo
label_nome = Label(frame_baixo, text='Login *',
                   anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
label_nome.place(x=10,y=20)
e_nome = Entry(frame_baixo, width=25, justify='left', font=("",15), 
                    highlightthickness=1,relief='solid')
e_nome.place(x=14,y=50)


label_pass = Label(frame_baixo, text='Password *',
                   anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
label_pass.place(x=10,y=95)
e_pass = Entry(frame_baixo, width=25, justify='left', show='*', font=("",15), 
                    highlightthickness=1,relief='solid')
e_pass.place(x=14,y=130)


confirmar = Button(frame_baixo, command=verificar_senha, text='Entrar *', width=39, height=2,
                   font=('Ivy 8 bold'), bg=co2, fg=co1, relief=RAISED, overrelief=RIDGE)
confirmar.place(x=15,y=180)

# Credenciais
credenciais = ['joao','1234']

def verificar_senha():
    nome = e_nome.get()
    senha = e_pass.get()

    if nome == 'admin' and senha == 'admin':
        messagebox.showinfo('Login Realizado_Bem-Vindo')
    elif credenciais[0] == nome and credenciais[1]==senha:
        messagebox.showinfo('Login Realizado_Bem-Vindo')
    else: 
        messagebox.showwarning('Erro - Login não realizado')
        

# método que inicia a janela gráfica, ela fica aberta até seja dado o comando de fechar, botão X.
janela.mainloop()
