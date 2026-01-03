from tkinter import *
from Radar_de_Velocidade.Teste.Atalhos import *


def CASA(e, ed1, janela1):
    t = ed1.get()
    more(f"select placa, velocidade, id, dia, hora, dds from tabela1 where placa like '{t}%' and placa not like 'Pendente%' order by id desc", CASA)
    search(janela1)
