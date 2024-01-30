import tkinter
from tkinter import * 
# the line above means to import tkinter and use all of 
# its widgets

''' Tkinter is used to make a GUI '''

class ParentWindow(Frame):
    # refeering to class as Master, and whats in the function as Self
    def __init__ (self, master):
        Frame.__init__(self)
        
        self.master = master
        self.master.resizable(width = True, height = True)
        self.master.geometry('{}x{}'.format(700, 400))
        self.master.title('Learning Tkinter!')
        #               back ground
        self.master.config(bg = 'dark grey')
        
        self.varFname = StringVar() 
        self.varLname = StringVar()
        
        # Labels for the entry boxes (lines 31 - 37)
        self.lblFname = Label(self.master, text = 'First Name', font = ('Helvetica', 16), fg = 'black', bg = 'lightgrey')
        self.lblFname.grid(row=0, column = 0, padx = (30,2), pady = (30, 2) )
        
        self.lblLname = Label(self.master, text = 'Last Name', font = ('Helvetica', 16), fg = 'black', bg = 'lightgrey')
        self.lblLname.grid(row=1, column = 0, padx = (30,2), pady = (30, 2))

        self.lblDisplay = Label(self.master, text = '', font = ('Helvetica', 16), fg = 'black', bg = 'lightgrey')
        self.lblDisplay.grid(row=3, column = 1, padx = (30,2), pady = (30, 2))
        
        # This line, we are passing in the way to build the text box with the 'Entry()' function, and we are setting it to 
        # self.txtFname
        self.txtFname = Entry(self.master, text = self.varFname, font = ('Helvetica', 16), fg = 'black', bg = 'lightblue')
        self.txtLname = Entry(self.master, text = self.varLname, font = ('Helvetica', 16), fg = 'black', bg = 'lightblue')
        # Now we will 'Paint it' onto the window 
        self.txtFname.grid(row= 0, column =1, padx = (30,2), pady = (30, 2))
        self.txtLname.grid(row= 1, column =1, padx = (30,2), pady = (30, 2))
        
        self.btnSubmit = Button(self.master, text = 'Submit', width = 5, height = 2, command = self.submit)
        self.btnSubmit.grid(row= 2, column = 1, padx = (0,0), pady = (30, 2), sticky = NE)
        
        self.btnCancel = Button(self.master, text = 'Cancel', width = 5, height = 2, command = self.cancel)
        self.btnCancel.grid(row= 2, column = 1, padx = (0,90), pady = (30, 2), sticky = NE)


    def submit(self):
        fn = self.varFname.get()
        ln = self.varLname.get()
        self.lblDisplay.config(text = 'Hello, {} {}!'.format(fn, ln))
    
    def cancel(self):
        self.master.destroy()





if __name__ == '__main__':
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()