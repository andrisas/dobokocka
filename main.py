from tkinter import *
from random import randint
def dob ():
    szöveg.delete(0.0, END)
    szöveg.insert(END, str(randint(1,6)))
ablak = Tk()
szöveg = Text(ablak, width=2, height=2)
gomb_A = Button(ablak, text='Nyomd meg!' , command =dob)
szöveg.pack()
gomb_A.pack()
