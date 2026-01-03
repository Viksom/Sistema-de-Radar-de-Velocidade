import mysql.connector
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Radar_de_Velocidade.Pagar import *
from Radar_de_Velocidade.Pendentes import *
from datetime import *

gui = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='base_de_dados1'
)

cursor = gui.cursor()
