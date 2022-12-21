#!/usr/bin/env python3
import tkinter as tk
from tkinter import *

def factorial(n):
    return 1 if (n==1 or n==0) else n*factorial(n-1)

def calculate():
    result = factorial(int(entryText.get()))
    info.config(text=result)

def clear():
        entryText.delete(0,'end')
        info.config(text='')

window = tk.Tk()
window.title("Factorial")
window.geometry("300x300")
window.resizable(0,0)

entryText = tk.Entry(window,bg='white',fg='black')
entryText.place(x=50,y=25,width=100,height=25)

btn = tk.Button(text='Calculate',command=calculate)
btn.place(x=50,y=75,width=100,height=25)

btn = tk.Button(text='Clear',command=clear)
btn.place(x=170,y=75,width=100,height=25)

info = tk.Label(bg='white',fg='red',anchor=SE)
info.place(x=50,y=125,width=200,height=30)

lbl=tk.Label(text="Thanks for using",relief = tk.FLAT)
lbl.place(x=50,y=175,width=150,height=25)

window.mainloop()
