# 4 - Utilizando a biblioteca gráfica Tkinter, o aluno deve construir uma interface que simule uma tela de
# login de usuário contendo o campo de login, senha e um botão de autenticação. (2,0 pontos).

from tkinter import *
from tkinter import Tk, ttk

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


# link https://www.youtube.com/watch?v=-8kvUOj3V8I

# método que inicia a janela gráfica, ela fica aberta até seja dado o comando de fechar, botão X.
janela.mainloop()
