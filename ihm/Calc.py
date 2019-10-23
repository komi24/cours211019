# -*- coding: utf-8 -*-
from CalcUI import CalcUI
from tkinter import StringVar


class Calc(CalcUI):
    def __init__(self):
        CalcUI.__init__(self)
        self.operande_1 = StringVar()
        self.operator = StringVar()
        self.operande_1.set("0")
        self.operator.set("+")
        self.from_enter = False
        
    def process(self, evt):
        op1 = int(self.operande_1.get())
        op2 = int(self.chaine.get())
        op = self.operator.get()
        res = ""
        if op == "+":
            res = str(op1 + op2)
        if op == "-":
            res = str(op1 - op2)
        if op == "*":
            res = str(op1 * op2)
        if op == "/":
            res = str(op1 // op2)
        if not self.from_enter:
            self.operande_1.set(res)
            self.from_enter = False
        return res
            
    def handle_number(self, evt):
        self.chaine.set(self.chaine.get() + evt.widget.cget("text"))
    
    def handle_op(self, evt):
        self.process(evt)
        self.operator.set(evt.widget.cget("text"))
        self.chaine.set("")
        
    def handle_enter(self, evt):
        res = self.process(evt)
        self.chaine.set(res)
        self.from_enter = True
        