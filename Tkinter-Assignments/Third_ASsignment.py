from tkinter import * 

win = Tk() 
lb = Listbox(win, height=3) 
lb.pack() 
# The 'END' means the entry box will be inserted at the end of the ListBox
lb.insert(END, 'First Entry')
lb.insert(END, 'Second Entry')
lb.insert(END, 'Third Entry')
lb.insert(END, 'Fourth Entry')
# The fourth entry doesnt show since the height is set to 3 

# Creating the scrollbar 
sb.Scrollbar(win, orient= VERTICAL)
sb.pack(side = Left, fill=y)
# Telling the scrollbar and the listbox about each other so the scrollbar moves the box
sb.configure(command=lb.yview)
lb.configure(command= sb.set)
