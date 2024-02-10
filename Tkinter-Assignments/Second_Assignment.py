from tkinter import * 
# import tkinter as tk 

# THIS IS SUPPOSED OT BE RAN IN IDLE BUT I DO NOT HAVE IT SO IM TYPING IT IN VSCODE

win = Tk()
v = StringVar()
e = Entry(win, textvariable = v)
e.pack()
v.get()

v.set('This is set by the program')