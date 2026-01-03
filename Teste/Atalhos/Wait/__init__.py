from Radar_de_Velocidade.Teste.Atalhos import *


def pend(janela1):
    global teste
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


def Ver_pendentes():
    try:
        obt = teste.selection()[0]
        val = teste.item(obt, 'values')
        inserir(val[0], val[1], val[2], val[3], val[4], val[5])
        ver_pend()
    except:
        messagebox.showinfo('Nota...', 'Selecione um Campo')
