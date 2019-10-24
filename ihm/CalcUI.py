# -*- coding: utf-8 -*-
from tkinter import Tk, Label, Button, Frame, StringVar
from tkinter import LEFT, RIGHT, TOP, BOTTOM


class CalcUI:
    def __init__(self):
        self.fen = Tk()
        self.chaine  =StringVar()
        self.chaine.set("")
        self.lbl = Label(self.fen, textvariable=self.chaine, height=3) #, width=100, height=50)
        self.lbl.pack(side=TOP)
        
        self.btn = Button(self.fen, text="ENTER", height=3)
        self.btn.pack(side=BOTTOM, expand=True, fill="both")
        self.btn.bind("<Button-1>", self.handle_enter)
        
        self.frame_op = Frame(self.fen)
        self.frame_op.pack(side=RIGHT)
        
        self.btn_zero = Button(self.fen, text="0")
        self.btn_zero.pack(side=BOTTOM, expand=True, fill="both")
        self.btn_zero.bind("<Button-1>", self.handle_number)
        
        self.frame_num = Frame(self.fen)
        self.frame_num.pack()
        for i, op in enumerate(["+", "-", "*", "/"]):
            btn = Button(self.frame_op, text=op, width=5, height=3)
            btn.pack()
            btn.bind("<Button-1>", self.handle_op)

        for i in range(3):
            for j in range(3):
                btn = Button(self.frame_num, text=f"{(10-3*(i+1))+j}", width=5, height=3)
                btn.grid(column=j, row=i)
                btn.bind("<Button-1>", self.handle_number)

        
    def handle_enter(self, evt):
        pass
        
    def handle_number(self, evt):
        pass

    def handle_op(self, evt):
        pass
        
    def start(self):
        self.fen.mainloop() 
        
        
        
        
        
        