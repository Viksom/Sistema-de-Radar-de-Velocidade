from Radar_de_Velocidade.Teste.Atalhos import *


def hoje(janela1):
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


def HOJE(e, ed1, app):
    hoje(app)
    t = ed1.get()
    z = date.today()
    day = str(z)
    more(f"select placa, velocidade, id, dia, hora, dds from tabela1 "
         f"where  dia = '{day}' and placa like '{t}%' and placa not like 'Pendente%' "
         f"order by id desc", HOJE)
