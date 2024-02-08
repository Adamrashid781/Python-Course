from tkinter import * 
import tkinter as tk 
from tkinter import messagebox 

import Functions 
import GUI 


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        
        # Define our master frame  configurations 
        self.master = master 
        self.master.minsize(700, 400)
        self.master.maxsize(1100, 700)
        
        
        # Center the window 
        Functions.center_window(self, 700, 400)
        self.master.title('Student Tracking')
        self.master.configure(bg = 'Indigo')
        
        # this protocol method is a tkinter built in method to catch if the user clicks the top left 
        # X to close the window 
        self.master.protocol('WM_DELETE_WINDOW', lambda: Functions.ask_quit(self))
        arg = self.master 
        
        GUI.load_gui(self)


if __name__ == '__main__':
    root = tk.Tk() 
    App = ParentWindow(root)
    root.mainloop()