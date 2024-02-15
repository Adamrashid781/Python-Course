import tkinter as tk 
from tkinter import * 
import webbrowser


class ParentWindow(Frame):
    def __init__(self,master):
        Frame.__init__(self, master)
        self.master.title('Web Page Generator')
        
        self.custom_entry_lbl = Label(self.master, text = 'Enter custom text or click the Default HTML page button')
        self.custom_entry_lbl.grid(row=1, column= 0, columnspan= 3, pady = (15, 0), sticky = N + E )
        
        self.custom_entry = Entry(self.master, text = '', width=40)
        self.custom_entry.grid(row=2, column=0, columnspan= 6, padx=(10,10), pady=(10,10), sticky = N )
        
        self.btn = Button(self.master, text = 'Default HTML Page', width=30, height = 2, command = self.defaultHTML)
        self.btn.grid( padx=(10,10), pady=(10, 10), sticky = S  )
        print('hello2')
        
        self.custom_button = Button(self.master, text = 'Submit Custom Text', width=30, height = 2, command = self.customText)
        self.custom_button.grid(padx=(10, 10), pady=(10,10), sticky = S  )
        
        
    def defaultHTML(self):
        print('hello')
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index_generator.html", "w")
        htmlContent = "<html>\n<Body>\n<h1>" + htmlText + "<h1>\n<body>\n<html>"
        print(htmlContent)
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index_generator.html")
    
    def customText(self):
        print('\nhello custom\n')
        htmlText = self.custom_entry.get()
        htmlFile = open('index_custom.html', 'w')
        htmlContent = "<html>\n<Body>\n<h1>" + htmlText + "<h1>\n<body>\n<html>"
        print(htmlContent)
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab('index_custom.html')

if __name__ =='__main__':
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop() 