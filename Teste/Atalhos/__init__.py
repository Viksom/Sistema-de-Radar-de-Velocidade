from Radar_de_Velocidade.Teste.Atalhos.base_dados import *


def more(cont, funcao):
    global w, z
    w = cont
    z = funcao


def search(janela1):
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


def pesq(janela1, ed1):
    global teste, t
    z(True, ed1, janela1)
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


def ver():
    try:
        obt = teste.selection()[0]
        val = teste.item(obt, 'values')
        insert(val[0], val[1], val[2], val[3], val[4], val[5])
        pagar()
    except:
        messagebox.showinfo('Nota...', 'Selecione um Campo')
