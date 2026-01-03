from tkinter import ttk
from Pagar import *
from Pendentes import *
import mysql.connector
from datetime import *
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

janela1 = Tk()
janela1.resizable(0, 0)

gui = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='base_de_dados1'
)

cursor = gui.cursor()
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def ver():
    try:
        obt = teste.selection()[0]
        val = teste.item(obt, 'values')
        insert(val[0], val[1], val[2], val[3], val[4], val[5])
        pagar()
    except:
        messagebox.showinfo('Nota...', 'Selecione um Campo')

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def Ver_pendentes():
    try:
        obt = teste.selection()[0]
        val = teste.item(obt, 'values')
        insert(val[0], val[1], val[2], val[3], val[4], val[5])
        ver_pend()
    except:
        messagebox.showinfo('Nota...', 'Selecione um Campo')

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def more(cont, funcao):
    global  w, z
    w = cont
    z = funcao

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def search():
    global teste
    #t = ed1.get()
    cursor.execute(w)
    cols = 'PLACA', 'VELOCIDADE', 'ID', 'DATA', 'HORA', 'DIA DA SEMANA'
    teste = ttk.Treeview(janela1, columns=cols, show='headings')
    teste.column(cols[0], minwidth=5, width=140)
    teste.column(cols[1], minwidth=5, width=120)
    teste.column(cols[2], minwidth=5, width=75, anchor=CENTER)
    teste.column(cols[3], minwidth=5, width=100, anchor=CENTER)
    teste.column(cols[4], minwidth=5, width=100, anchor=CENTER)
    teste.column(cols[5], minwidth=5, width=115)

    for col in cols:
        teste.heading(col, text=col)
        teste.place(x=350, y=350)
    for c in cursor:
        teste.insert("", "end", values=(c[0], f'{c[1]} km/h', c[2], c[3], c[4], c[5]))
        teste.bind('<Double-Button-1>')
    bt8 = Button(janela1, width=15, text='Abrir', bg='grey', fg='white', command=ver)
    bt8.place(x=620, y=650)

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def pesq(e):
    global teste, t
    z(True)
    cursor.execute(w)
    cols = 'PLACA', 'VELOCIDADE', 'ID', 'DATA', 'HORA', 'DIA DA SEMANA'
    teste = ttk.Treeview(janela1, columns=cols, show='headings')
    teste.column(cols[0], minwidth=5, width=140)
    teste.column(cols[1], minwidth=5, width=120)
    teste.column(cols[2], minwidth=5, width=75, anchor=CENTER)
    teste.column(cols[3], minwidth=5, width=100, anchor=CENTER)
    teste.column(cols[4], minwidth=5, width=100, anchor=CENTER)
    teste.column(cols[5], minwidth=5, width=115)

    for col in cols:
        teste.heading(col, text=col)
        teste.place(x=350, y=350)
    for c in cursor:
        teste.insert("", "end", values=(c[0], f'{c[1]} km/h', c[2], c[3], c[4], c[5]))
        teste.bind('<Double-Button-1>')
    bt8 = Button(janela1, width=15, text='Abrir', bg='grey', fg='white', command=ver)
    bt8.place(x=620, y=650)

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def hoje():
    global teste, day
    q = date.today()
    day = str(q)
    cursor.execute(f"select placa, velocidade, id, dia, hora, dds from tabela1 where dia = '{day}' and placa not like 'Pendente%'")
    cols = 'PLACA', 'VELOCIDADE', 'ID', 'DATA', 'HORA', 'DIA DA SEMANA'
    teste = ttk.Treeview(janela1, columns=cols, show='headings')
    teste.column(cols[0], minwidth=5, width=140)
    teste.column(cols[1], minwidth=5, width=120)
    teste.column(cols[2], minwidth=5, width=75, anchor=CENTER)
    teste.column(cols[3], minwidth=5, width=100, anchor=CENTER)
    teste.column(cols[4], minwidth=5, width=100, anchor=CENTER)
    teste.column(cols[5], minwidth=5, width=115)

    for col in cols:
        teste.heading(col, text=col)
        teste.place(x=350, y=350)
    for c in cursor:
        teste.insert("", "end", values=(c[0], f'{c[1]} km/h', c[2], c[3], c[4], c[5]))
        teste.bind('<Double-Button-1>')
    bt8 = Button(janela1, width=15, text='Abrir', bg='grey', fg='white', command=ver)
    bt8.place(x=620, y=650)

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def HOJE(e):
    hoje()
    t = ed1.get()
    z = date.today()
    day = str(z)
    more(f"select placa, velocidade, id, dia, hora, dds from tabela1 where  dia = '{day}' and placa like '{t}%' and placa not like 'Pendente%' order by id desc", HOJE)

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def CASA(e):
    t = ed1.get()
    more(f"select placa, velocidade, id, dia, hora, dds from tabela1 where placa like '{t}%' and placa not like 'Pendente%' order by id desc", CASA)
    search()

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def H():
    HOJE(True)

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def C():
    CASA(True)

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def pend():
    cursor.execute("select placa, velocidade, id, dia, hora, dds from tabela1 where placa like 'Pendente%' order by dia desc")
    cols = 'PLACA', 'VELOCIDADE', 'ID', 'DATA', 'HORA', 'DIA DA SEMANA'
    teste = ttk.Treeview(janela1, columns=cols, show='headings')
    teste.column(cols[0], minwidth=5, width=140)
    teste.column(cols[1], minwidth=5, width=120)
    teste.column(cols[2], minwidth=5, width=75, anchor=CENTER)
    teste.column(cols[3], minwidth=5, width=100, anchor=CENTER)
    teste.column(cols[4], minwidth=5, width=100, anchor=CENTER)
    teste.column(cols[5], minwidth=5, width=115)

    for col in cols:
        teste.heading(col, text=col)
        teste.place(x=350, y=350)
    for c in cursor:
        teste.insert("", "end", values=(c[0], f'{c[1]} km/h', c[2], c[3], c[4], c[5]))
        teste.bind('<Double-Button-1>')
    bt8 = Button(janela1, width=15, text='Abrir', bg='grey', fg='white', command=Ver_pendentes)
    bt8.place(x=620, y=650)

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def criar():
    global ed1
    png = PhotoImage(file="Icones/exp.png")
    imagem = PhotoImage(file="Icones/tam64.png")
    lbi = Label(janela1, image=png, bg='black', width=800)
    lbi1 = Label(janela1, image=png, bg='black', width=800)
    lba = Label(janela1, image=imagem, bg='black')
    ass = Label(janela1, text='Alberto & Paxe', bg='black', fg='black', font='Consolas 8 bold')
    ass.pack(side=BOTTOM, anchor=SE)
    lb = Label(janela1, text='GESTOR DE MULTAS', fg='red', width=90, bg='black', font='Consolas 14 bold')
    lbi.place(x=-100, y=0)
    lbi1.place(x=670, y=0)
    lba.place(x=650, y=178)
    lb.place(x=220, y=275)
    ed1 = Entry(janela1, font='yellow')
    ed1['width'] = 55
    ed1.place(x=350, y=310)
    CASA(False)
    search()

    my_menu = Menu(janela1, bg='red')
    janela1.config(menu=my_menu)
    item = Menu(my_menu)
    my_menu.add_cascade(label='Ver', menu=item)
    item.add_command(label='Casa', command=C)
    item.add_command(label='Pendentes', command=pend)
    item.add_command(label='Hoje', command=H)
    item.add_command(label='Sair', command=janela1.destroy)

    bt = Button(janela1, width=20, text='Pesquisar', bg='grey', fg='white', command=search)
    bt.place(x=852, y=308)
    ed1.bind('<KeyRelease>', pesq)

    janela1.title('Gestor de Multas')
    janela1['bg'] = 'light blue'
    janela1.geometry('1305x715+-10+0')
    janela1.iconbitmap('Icones/icon.ico')
    janela1.mainloop()

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-


criar()
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
