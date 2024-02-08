import os 
from tkinter import * 
import tkinter as tk 
from tkinter import messagebox 
import sqlite3 

import Main 
import GUI 



def center_window( self, w, h):
    # grab the users screen width and height 
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    # calculate the x and y and paint the app onto the center of the window 
    x = int((screen_width / 2) - (w/2))
    y = int((screen_height / 2) - (w/2))
    
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo 

def ask_quit(self):
    if messagebox.askokcancel('Exit Program', 'Okay to exit application?'): 
        # This will close the app
        self.master.destroy()
        os._exit(0)

def create_db(self):
    print('We are entering the create db function')
    conn = sqlite3.Connection('student_tracking.db')
    with conn: 
        cur = conn.cursor()
        cur.execute('CREATE TABLE if not exists tbl_students( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fname TEXT, \
            col_lname TEXT, \
            col_fullname TEXT, \
            col_phone TEXT, \
            col_email TEXT, \
            col_current_course TEXT \
            ); ')
        # Always commit changes when tapping into the db
        conn.commit()
    conn.close()
    first_run(self)

def first_run(self):
    conn = sqlite3.connect('student_tracking.db')
    with conn :
        cur = conn.cursor()
        cur,count = count_records(cur)
        if count < 1:
            cur.execute("""INSERT INTO tbl_students (col_fname, col_lname, col_fullname, col_phone, col_email, col_current_course) VALUES (?,  ?, ?, ?, ?, ?)""", ('John', 'Doe', 'John Doe', '2091112244', 'JDoe@gmail.com', 'Math') )
            conn.commit()
    conn.close()

def count_records(cur):
    count = ''
    cur.execute('SELECT COUNT(*) FROM tbl_students')
    count = cur.fetchone()[0]
    return cur, count

def onSelect(self, event):
    # Calling the event is the self.lstList1 widget 
    varList = event.widget 
    select = varList.curselection()[0]
    value = varList.get(select)
    conn = sqlite3.connect('student_tracking.db')
    with conn: 
        cursor = conn.cursor()
        cursor.execute('SELECT col_fname, col_lname, col_phone, col_email, col_current_course FROM tbl_students WHERE col_fullname = (?)', [value])
        varBody = cursor.fetchall()
        print(varBody   )
        # This returns a tuple and we can slice it into 5 parts using the data[] during the iteration
        for data in varBody:
            self.txt_fname.delete(0, END)
            self.txt_fname.insert(0, data[0])
            self.txt_lname.delete(0, END)
            self.txt_lname.insert(0, data[1])
            self.txt_phone.delete(0, END)
            self.txt_phone.insert(0, data[2])
            self.txt_email.delete(0, END)
            self.txt_email.insert(0,data[3])
            self.txt_current_course.delete(0, END)
            self.txt_current_course.insert(0, data[4])

def addToList(self):
    print('We are entering the addToList Function')
    var_fname = self.txt_fname.get()
    var_lname = self.txt_lname.get()
    
    # Normalizing the data now to keep it consistent in the database 
    var_fname = var_fname.strip() # THis will remove any blank spaces before or after the users entry 
    var_lname = var_lname.strip() 
    var_fname = var_fname.title() # this will capitalize the first letter of each name 
    var_lname = var_lname.title()
    
    var_fullname = ('{} {}'.format(var_fname, var_lname)) # To combine the names into a full name 
    print('var_fullname: {}'.format(var_fullname))
    var_phone = self.txt_phone.get().strip()
    var_email = self.txt_email.get().strip()
    var_current_course = self.txt_current_course.get().strip()
    if not '@' or not '.' in var_email: 
        print('Incorrect email format!!!')
    if (len(var_fname) > 0) and (len(var_lname) > 0) and (len(var_phone) > 0) and (len(var_email) > 0) and (len(var_current_course) > 0):
        conn = sqlite3.connect('student_tracking.db')
        with conn:
            cursor = conn.cursor()
            
            # check the database for existance of a full name, if so we will alert the user and disregard the request 
            cursor.execute("""SELECT COUNT(col_fullname) FROM tbl_students WHERE col_fullname = '{}' """.format(var_fullname))
            count = cursor.fetchone()[0]
            chkName = count
            print('count = ' + str(count))
            if chkName == 0: # if this is 0 then there is no existance of the full name and we add new data 
                print('chkName: {}'.format(chkName))
                cursor.execute('''INSERT INTO tbl_students (col_fname, col_lname, col_fullname, col_phone, col_email, col_current_course) VALUES (?, ?, ?, ?, ?, ?)''', (var_fname, var_lname, var_fullname, var_phone, var_email, var_current_course))
                self.lstList1.insert(END, var_fullname) # Update the list box with the data clicked on
                # onClear(self)
            else: 
                messagebox.showerror('Name Error', "'{}' already exists in the database! Please choose a different name.".format(var_fullname))
                onClear(self) # Will cleat the text boxes
        conn.commit()
        conn.close()
    else: 
        messagebox.showerror('Missing Text Error', 'Please ensure that there is data in all five fields!')


def onDelete(self):
    var_select = self.lstList1.get(self.lstList1, curselection()) # the selected value in the list box
    conn = sqlite3.connect('student_tracking.db')
    with conn: 
        cur = conn.cursor()
        confirm = messagebox.askokcancel('Delete Confirmation', "All information associated with, '{}' \nwill be permenantly deleted from the database \
                                            \nProceed with the deletion Request?".format(var_select))
        if confirm: 
            conn = sqlite3.connect('student_tracking.db')
            with conn: 
                cur = conn.cursor() 
                cursor.execute('''DELETE FROM tbl_students WHERE col_fullname = '{}' '''.format(var_fullname))
            onDeleted(self) # Call the function to clear all of the text boxes and the selected index of listbox
            onRefresh(self) # Update the listbox of the changes
            conn.commit()
    conn.close()

def onDeleted(self):
    # clears the text in these text boxes 
    self.txt_fname.delete(0, END)
    self.txt_lname.delete(0, END)
    self.txt_phone.delete(0, END)
    self.txt_email.delete(0, END)
    self.txt_current_course(0, END)
    onRefresh(self) # update the list box
    
    try: 
        index = self.lstList1.curselection()[0]
        self.lstList1.delete(index)
    except IndexError:
        pass

def onClear(self):
    # Clear the text in these boxes 
    self.txt_fname.delete(0, END)
    self.txt_lname.delete(0, END)
    self.txt_phone.delete(0, END)
    self.txt_email.delete(0, END)
    self.txt_current_course(0, END)


def onRefresh(self):
    # Populate the listboxes with the data from the database 
    self.lstList1.delete(0, END)
    conn = sqlite3.connect('student_tracking.db')
    with conn: 
        cur = conn.cursor()
        cur.execute('SELECT COUNT(*) FROM tbl_students')
        count = cur.fetchone()[0]
        i = 0
        while i < count:
            cur.execute('SELECT col_fullname FROM tbl_students')
            varList = cur.fetchall()[i]
            for item in varList:
                self.lstList1.insert(0, str(item))
                i += 1
    conn.close()


if __name__ == '__main__':
    pass
