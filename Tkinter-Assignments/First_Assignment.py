from tkinter import * 



# THIS IS SUPPOSED OT BE RAN IN IDLE BUT I DO NOT HAVE IT SO IM TYPING IT IN VSCODE
win = Tk()

# Simple buttons
b1 = Button(win, text='One')
b2 = Button(win, text='Two')
# b1.pack(side=LEFT, padx = 10 )
# b2.pack(side=LEFT, padx = 10 )

b1.grid(row = 0, column = 0)
b2.grid(row = 1, column = 1)

l = Label(win, text='This is a label')
l.grid(row=1, column=0)

b1.configure(text='Uno')

def but1():
    print('Button one was pushed')

b1.configure(commant=but1())