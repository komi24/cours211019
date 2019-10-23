# -*- coding: utf-8 -*-

from tkinter import Tk, Label, Button, Frame, StringVar
from tkinter import LEFT, RIGHT, TOP, BOTTOM


fen = Tk()

"""
    1- Récupérer les chiffres sur lesquels on cliqué
    2- Afficher les chiffres les uns à la suite des autres
    3- Ajouter la gestion de l'opération
"""
def change_label(evt):
    old_value = a.get()
    a.set(evt.widget.cget("text"))
  
  
a = StringVar()
a.set("Bonjour")

lbl = Label(fen, textvariable=a, height=3) #, width=100, height=50)
lbl.pack(side=TOP)

btn = Button(fen, text="ENTER", height=3)
btn.pack(side=BOTTOM, expand=True, fill="both")
btn.bind("<Button-1>", change_label)

frame_op = Frame(fen)
frame_op.pack(side=RIGHT)

btn_zero = Button(fen, text="0")
btn_zero.pack(side=BOTTOM, expand=True, fill="both")
btn_zero.bind("<Button-1>", change_label)

frame_num = Frame(fen)
frame_num.pack()

#btn = Button(fen, text="B")
#btn.pack(side=RIGHT, expand=True, fill="both")
#
#btn2 = Button(fen, text="Bouton 2")
#btn2.grid()
for i, op in enumerate(["+", "-", "*", "/"]):
    btn = Button(frame_op, text=op, width=5, height=3)
    btn.pack()

for i in range(3):
    for j in range(3):
        btn = Button(frame_num, text=f"{(10-3*(i+1))+j}", width=5, height=3)
        btn.grid(column=j, row=i)

print("avant")
fen.mainloop()
print("apres")

a.set("12")

