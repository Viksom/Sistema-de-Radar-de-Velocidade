from tkinter import *

X = (200 - 20) / 2
Y = (400 - 40) / 2

root = Tk()

center = LabelFrame(root, width=20, height=40, background="yellow").place(x= X, y=Y)

root.geometry("200x400+100+100")
root.mainloop()