import tkinter
from tkinter import *
from Atalhos.Home import *
from Atalhos import *
from functools import partial
from Atalhos.Wait import *
from Atalhos.Today import *


def atalho(e):
    pesq(janela1, ed1)


def more(cont, funcao):
    global w, z
    w = cont
    z = funcao


janela1 = Tk()
janela1.resizable(0, 0)
png = PhotoImage(file="Icones/exp.png")
imagem = PhotoImage(file="Icones/tam64.png")
lbi = Label(janela1, image=png, bg='black', width=800)
lbi1 = Label(janela1, image=png, bg='black', width=800)
lba = Label(janela1, image=imagem, bg='black')
ass = Label(janela1, text='Alberto & Paxe', bg='black', fg='red', font='Consolas 8 bold')
ass.pack(side=BOTTOM, anchor=SE)
lb = Label(janela1, text='GESTOR DE MULTAS', fg='red', width=90, bg='black', font='Consolas 14 bold')
lbi.place(x=-100, y=0)
lbi1.place(x=670, y=0)
lba.place(x=650, y=178)
lb.place(x=220, y=275)
ed1 = Entry(janela1, font='yellow')
ed1['width'] = 55
ed1.place(x=350, y=310)
CASA(True, ed1, janela1)


def C():
    CASA(True, ed1, janela1)


def H():
    HOJE(True, ed1, janela1)


search(janela1)

my_menu = Menu(janela1, bg='red')
janela1.config(menu=my_menu)
item = Menu(my_menu)
my_menu.add_cascade(label='Ver', menu=item)
item.add_command(label='Início', command=C)
item.add_command(label='Pendentes', command=partial(pend, janela1))
item.add_command(label='Hoje', command=H)
item.add_command(label='Sair', command=janela1.destroy)

bt = Button(janela1, width=20, text='Pesquisar', bg='grey', fg='white', command=partial(search, janela1))
bt.place(x=852, y=308)

ed1.bind('<KeyRelease>', atalho)

janela1.title('Gestor de Multas')
janela1['bg'] = 'light blue'
janela1.geometry('1305x715+-10+0')
janela1.iconbitmap('Icones/icon.ico')
janela1.mainloop()
