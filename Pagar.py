from tkinter import *
from tkinter import messagebox
import mysql.connector

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

gui = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='base_de_dados1'
)

cursor = gui.cursor()
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-


class insert():
    def __init__(self, placa, velocidade, multa, data, hora, d_semana):
        global p, v, m, d, h, s, fotoNome
        p = self.pla = placa
        cursor.execute(f"select nome_foto from tabela1 where placa = '{p}'")
        for i in cursor:
            fotoNome = i
        v = self.vel = velocidade
        m = self.mul = multa
        d = self.date = data
        h = self.time = hora
        s = self.semana = d_semana
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-


def ver():
    global see
    janela2.destroy()
    try:
        see.destroy()
    except:
        pass
    see = Toplevel()
    see.overrideredirect(True)

    look = PhotoImage(file=f"Fotos\\{fotoNome[0]}")
    foto = PhotoImage(file='Icones/back.png')
    lb = Label(see, image=look).pack()
    bt = Button(see, image=foto, bg='darkgrey', command=retornar).place(x=0, y=0)

    see['bg'] = 'grey'
    see.geometry('+50+50')
    see.mainloop()
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-


def retornar():
    see.destroy()
    pagar()
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-


def pago():
    cursor.execute(f"delete from tabela1 where id = {m}")
    bt3 = Button(janela2, width=10, text='Pago', bg='green')
    bt3.place(x=200, y=250)
    messagebox.showinfo('Info', 'Multa Paga!')
    janela2.destroy()
    #search()
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-


def pagar():
    global d, janela2
    try:
        janela2.destroy()
    except:
        pass
    try:
        janela2 = Toplevel()
        #janela2.overrideredirect(True)

        png = PhotoImage(file="Icones/exp.png")
        gnp = PhotoImage(file='Icones/tam64.png')
        lba = Label(janela2, image=png, bg='black', width=800)
        lba.place(x=0, y=-20)
        lbn = Label(janela2, image=gnp, bg='black').place(x=400, y=130)
        ass = Label(janela2, text='Alberto & Paxe', bg='black', fg='red', font='Consolas 8 bold')
        ass.pack(side=BOTTOM, anchor=SE)
        my_menu = Menu(janela2)
        janela2.config(menu=my_menu)
        item1 = Menu(my_menu)
        my_menu.add_cascade(label='File', menu=item1)
        item1.add_command(label="Sair", command=janela2.destroy)

        et1 = Entry(janela2, width=40)
        et2 = Entry(janela2, width=40)
        et3 = Entry(janela2, width=40)
        et4 = Entry(janela2, width=40)
        et5 = Entry(janela2, width=40)
        et6 = Entry(janela2, width=40)

        et1.insert(END, p)
        et2.insert(END, v)
        et3.insert(END, m)
        et4.insert(END, d)
        et5.insert(END, h)
        et6.insert(END, s)

        et1.configure(state=DISABLED)
        et2.configure(state=DISABLED)
        et3.configure(state=DISABLED)
        et4.configure(state=DISABLED)
        et5.configure(state=DISABLED)
        et6.configure(state=DISABLED)

        bt2 = Button(janela2, width=10, text='Ver imagem', bg='grey', command=ver)
        bt3 = Button(janela2, width=10, text='Pagar', bg='grey', command=pago)
        et1.place(x=45, y=70)
        et2.place(x=45, y=110)
        et3.place(x=45, y=150)
        et4.place(x=45, y=190)
        et5.place(x=45, y=230)
        et6.place(x=45, y=270)
        bt2.place(x=400, y=300)
        bt3.place(x=500, y=300)

        janela2.resizable(0, 0)
        janela2.iconbitmap('Icones/icon.ico')
        janela2.geometry('600x350+50+50')
        janela2.title('Pagamento')
        janela2.mainloop()
    except:
        messagebox.showinfo('Erro', 'Não conseguimos abrir a tela.')
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-