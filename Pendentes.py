from tkinter import *
from tkinter import messagebox
import mysql.connector
from Radar_de_Velocidade.Envio import enviar_email
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
gui = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='base_de_dados1'
)

cursor = gui.cursor()
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-


class inserir():
    def __init__(self, placa, velocidade, multa, data, hora, d_semana):
        global p, v, m, d, h, s
        p = placa
        v = velocidade
        m = multa
        d = data
        h = hora
        s = d_semana
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-


def img():
    fotografiaPendente = ''
    cursor.execute(f"select nome_foto from tabela1 where placa = '{p}' and hora = '{h}'")
    for c in cursor:
        fotografiaPendente = c
    return fotografiaPendente[0]


def info():
    label = Label(janela2, bg='darkgrey').pack()
    cursor.execute(f"select placa, nome, email from registo where placa = {et1.get()}")
    K = ''
    for c in cursor:
        K = c
    if len(K) == 0:
        botao = Button(janela2, bg='red', text='i').pack()
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-


def notif():
    cursor.execute(f"select placa, nome, email from registo where placa = {et1.get()}")
    K = ''
    for c in cursor:
        K = c
    if len(K) > 0:
        enviar_email(K[1], K[0], et2.get(), et3.get(), K[2])
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-


def ver():
    global see
    try:
        see.destroy()
    except:
        pass
    see = Toplevel()
    see.overrideredirect(True)

    look = PhotoImage(file=f"Fotos/{img()}")
    foto = PhotoImage(file='Icones/back.png')
    lb = Label(see, image=look).pack()
    bt = Button(see, image=foto, bg='darkgrey', command=retornar).place(x=0, y=0)
    see['bg'] = 'grey'
    see.geometry('+200+50')
    see.mainloop()
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-


def retornar():
    see.destroy()
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-


def salvo():
    v = et1.get()
    cursor.execute(f"update tabela1 set placa = {v} where id = {m}")
    bt3 = Button(janela2, width=10, text='Pago', bg='green')
    bt3.place(x=200, y=250)
    notif()
    messagebox.showinfo('Info', 'Dado Salvo!')
    janela2.destroy()
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-


def editar():
    et1.configure(state=NORMAL)
    et1.bind('<KeyRelease>')
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-


def ver_pend():
    global d, janela2, et1, et2, et3, png, gnp
    try:
        janela2.destroy()
    except:
        pass

    try:
        janela2 = Toplevel()
        janela2.resizable(0, 0)
        janela2.iconbitmap('Icones/icon.ico')
        janela2.geometry('600x350+50+50')
        janela2.title('Pagamento')

        png = PhotoImage(file="Icones/exp.png")
        gnp = PhotoImage(file='Icones/tam64.png')
        lba = Label(janela2, image=png, bg='black', width=800)
        lba.place(x=0, y=-20)
        lbn = Label(janela2, image=gnp, bg='black')
        lbn.place(x=400, y=130)
        ass = Label(janela2, text='Alberto & Paxe', bg='black', fg='red', font='Consolas 8 bold')
        ass.pack(side=BOTTOM, anchor=SE)
        my_menu = Menu(janela2)
        janela2.config(menu=my_menu)
        item1 = Menu(my_menu)
        my_menu.add_cascade(label='Opções', menu=item1)
        item1.add_command(label='Editar', command=editar)
        item1.add_separator()
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
        bt3 = Button(janela2, width=10, text='Salvar', bg='grey', command=salvo)
        
        et1.place(x=45, y=70)
        et2.place(x=45, y=110)
        et3.place(x=45, y=150)
        et4.place(x=45, y=190)
        et5.place(x=45, y=230)
        et6.place(x=45, y=270)
        bt2.place(x=400, y=270)
        bt3.place(x=500, y=270)

        janela2.mainloop()
    except:
        messagebox.showinfo('Erro', 'Não conseguimos abrir a tela.')
        try:
            pass
            #janela2.destroy()
        except:
            pass
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
