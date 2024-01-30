
import os
from tkinter import *
import tkinter as tk 
from tkinter import messagebox
import sqlite3 


import Main 
import GUI 

def center_window(self, w, h): # Pass in the tkinter frame (master) reference and the W and H
    # Get users screen width and height 
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    # calculate x and y coordinates to paint the app centered on the user's screen 
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo

# Catch if the user clicks on the windows upper-right 'X' to ensure they want to close 
def ask_quit(self):
    if messagebox.askokcancel('Exit program', 'Okay to exit application?'):
        #this closes app
        self.master.destroy()
        os._exit(0)

######################################################################################################
def create_db(self):
    conn = sqlite3.connect('phonebook.db')
    with conn:
        cur = conn.cursor()
        cur.execute('CREATE TABLE if not exists tbl_phonebook( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fname TEXT, \
            col_lname TEXT, \
            col_fullname TEXT, \
            col_phone TEXT, \
            col_email TEXT \
            );')
        # You must commit() to save changes and close the database connection 
        conn.commit()
    conn.close() 
    first_run(self)

def first_run(self):
    conn = sqlite3.connect('phonebook.db')
    with conn:
        cur = conn.cursor() 
        cur,count = count_records(cur)
        if count < 1:
            cur.execute("""INSERT INTO tbl_phonebook (col_fname,col_lname,col_fullname,col_phone,col_email) VALUES (?,?,?,?,?)""", ('John','Doe','John Doe','111-111-1111','jdoe@email.com'))
            conn.commit()
    conn.close() 

def count_records(cur):
    count = ''
    cur.execute('SELECT COUNT(*) FROM tbl_phonebook')
    count = cur.fetchone()[0]
    return cur, count

# Select item in list 
def onSelect(self, event):
    # calling the event is the self.lstList1 widget
    varList = event.widget
    select = varList.curselection()[0]
    value = varList.get(select)
    conn = sqlite3.connect('phonebook.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute('SELECT col_fname, col_lname, col_phone, col_email FROM tbl_phonebook WHERE col_fullname = (?)', [value])
        varBody = cursor.fetchall()
        # This returns a tuple and we can slice it into 4 parts using data[] during the iteration 
        for data in varBody:
            self.txt_fname.delete(0, END)
            self.txt_fname.insert(0, data[0])
            self.txt_lname.delete(0, END)
            self.txt_lname.insert(0, data[1])
            self.txt_phone.delete(0, END)
            self.txt_phone.insert(0, data[2])
            self.txt_email.delete(0, END)
            self.txt_email.insert(0, data[3])

def addToList(self):
    print('We are entering the addToList Function')
    var_fname = self.txt_fname.get()
    var_lname = self.txt_lname.get()
    # normalize the data to keep it consistent int the database 
    var_fname = var_fname.strip() # This will remove any blank spaces before and after the user's entry 
    var_lname = var_lname.strip()
    var_fname = var_fname.title() # This will ensure that the first character in each word is capitalized 
    var_lname = var_lname.title()
    var_fullname = ('{} {}'.format(var_fname, var_lname)) # combine our normalized names into a full name
    print('var_fullname: {}'.format(var_fullname))
    var_phone = self.txt_phone.get().strip()
    var_email = self.txt_email.get().strip()
    if not '@' or not '.' in var_email: # Will use this soon
        print('Incorrect email format!!!')
    if (len(var_fname) > 0) and (len(var_lname) > 0) and (len(var_phone) > 0) and (len(var_email) > 0): #Enforce the user to provide both names
        conn = sqlite3.connect('phonebook.db')
        with conn:
            cursor = conn.cursor()
            # Check the database for existance of the full name, if so we will alert the user and disregard request 
            cursor.execute("""SELECT COUNT(col_fullname) FROM tbl_phonebook WHERE col_fullname = '{}' """.format(var_fullname))
            count = cursor.fetchone()[0]
            chkName = count 
            if chkName == 0: # If this is 0 then there is no existance of the fullname and we can add new data
                print('chkName: {}'.format(chkName))
                cursor.execute('''INSERT INTO tbl_phonebook (col_fname, col_lname, col_fullname, col_phone, col_email) VALUES (?, ?, ?, ?, ?)''', (var_fname,var_lname,var_fullname,var_phone,var_email))
                self.lstList1.insert(END, var_fullname) # Update listbox with the new fullname
                onClear(self) # call the function to clear all of the textboxes 
            else: 
                messagebox.showerror('Name Error',"'{}' already exists in the database! Please choose a different name.".format(var_fullname))
                onClear(self) #call the function to clear all of the textboxes
        conn.commit()
        conn.close()
    else:
        messagebox.showerror('Missing Text Error', 'Please ensure that there is data in all four fields.')

def onDelete(self):
    var_select = self.lstList1.get(self.lstList1.curselection()) # Listbox's selected value 
    conn = sqlite3.connect('phonebook.db')
    with conn:
        cur = conn.cursor()
        # Check count to ensure that this is not the last record in 
        # the database... cannot delete last record or we will get an error 
        cur.execute("""SELECT COUNT(*) FROM tbl_phonebook""")
        count = cur.fetchone()[0]
        if count > 1: 
            confirm = messagebox.askokcancel('Delete Confirmation', 'All information associated with, ({}) \
                \n will be permenantly deleted from the database/ \nProceed with the deletion request?'.format(var_select))
            if confirm:
                conn = sqlite3.connect('phonebook.db')
                with conn:
                    cursor = conn.cursor()
                    cursor.execute('''DELETE FROM tbl_phonebook WHERE col_fullname = '{}' '''.format(var_select))
                onDeleted(self) # Call the function to clear all of the textboxes and the selected index of listbix
                onRefresh(self) # Update the listbox of the changes
                conn.commit()
        else:
            confirm = messagebox.showerror('Last Record Error', '({}) is the last record in the database and cannot be deleted at this time. \
                                            \n please add another record first before you can delete ({}).'.format(var_select, var_select))
    conn.close()

def onDeleted(self):
    # Clear the text in these text boxes
    self.txt_fname.delete(0, END)
    self.txt_lname.delete(0, END)
    self.txt_phone.delete(0, END)
    self.txt_email.delete(0, END)
    
    # onRefresh(self) #update the list box
    
    try:
        index = self.lstList1.curselection()[0]
        self.lstList1.delete(index)
    except IndexError:
        pass


def onClear(self):
    # Clear the text in these text boxes
    self.txt_fname.delete(0, END)
    self.txt_lname.delete(0, END)
    self.txt_phone.delete(0, END)
    self.txt_email.delete(0, END)

def onRefresh(self):
    # Populate the listbox, coinciding with the database 
    self.lstList1.delete(0, END)
    conn = sqlite3.connect('phonebook.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT (*) FROM tbl_phonebook')
        count = cursor.fetchone()[0]
        i = 0
        while i < count: 
            cursor.execute('SELECT col_fullname FROM tbl_phonebook')
            varList = cursor.fetchall()[i]
            for item in varList:
                self.lstList1.insert(0, str(item))
                i += 1
    conn.close()


def onUpdate(self):
    try: 
        var_select = self.lstList1.curselection()[0] # Index of the list selection 
        var_value = self.lstList1.get(var_select) # list selection's text value
    except: 
        messagebox.showinfo('Missing selection', 'No name was selected from the list box. \nCancelling the Update request.')
        return 
    # The user will only be allowed to update changes for phone and emails.
    # For name changes, the user will need to delete the entire record and start over.
    var_phone = self.txt_phone.get().strip() # Normalize the data to maintain database integrity 
    var_email = self.txt_email.get().strip()
    if (len(var_phone) > 0) and (len(var_email) > 0): # ensure that there is data present 
        conn = sqlite3.connect('phonebook.db')
        with conn:
            cur = conn.cursor()
            # count records to see if the user's changes are already in 
            # the database.... meaning, there are no changes to update.
            cur.execute('''SELECT COUNT(col_phone) FROM tbl_phonebook WHERE col_phone = '{}' '''.format(var_phone))
            count = cur.fetchone()[0]
            print(count)
            cur.execute("""SELECT COUNT(col_email) FROM tbl_phonebook WHERE col_email = '{}'""".format(var_email))
            count2 = cur.fetchone()[0] 
            print(count2)
            if count == 0 or count2 == 0: # if proposed changes are not already in the database, then proceed
                response = messagebox.askokcancel('Update request', 'The following changes ({}) and ({}) will be implemented for \
                                                    ({}). \nProceed with the update request?'.format(var_phone, var_email, var_value))
                print(response)
                if response:
                    with conn:
                        print('We are entereing the conn')
                        # print('These are the upated values going in {}, {}, {}, {} '.format(var_fname, var_))
                        cursor = conn.cursor()
                        cmd = """UPDATE tbl_phonebook SET col_phone = '{}', col_email = '{}' WHERE col_fullname = '{}' """.format(var_phone, var_email, var_value)
                        print(cmd) 
                        cursor.execute("""UPDATE tbl_phonebook SET col_phone = '{}', col_email = '{}' WHERE col_fullname = '{}' """.format(var_phone, var_email, var_value))
                        conn.commit()
                        onClear(self)
                        onRefresh(self)
                else: 
                    messagebox.showinfo("Cancel request", "No changes have been made to ({}).".format(var_value))
            else:
                messagebox.showinfo("No changes detected", "Both ({}) and ({}) \nalready exist in the database for this name.\n\nYour update has been cancelled.".format(var_phone, var_email))
            onClear(self)
        conn.close()
    else: 
        messagebox.showerror("Missing information", "Please select a name from the list.\nThen edit the phone or email information.")
    # onClear(self)

if __name__ == '__main__':
    pass