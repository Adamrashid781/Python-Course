import sqlite3

# print(help(sqlite3))

# This var will hold the connection to the DataBase
#conn = sqlite3.connect("test.db")
conn = sqlite3.connect("test.db")

with conn :
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_persons(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fname TEXT, \
        col_lname TEXT, \
        col_email TEXT \
        )")
    conn.commit()
conn.close()

conn = sqlite3.connect("test.db")
with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_persons(col_fname, col_lname, col_email) VALUES (?, ?, ?)", \
        ('Adam', 'Sandler', 'asandler@gmail.com'))
    # cur.execute("INSERT INTO tbl_persons(col_fname, col_lname, col_email) VALUES (?, ?, ?)", \
    #     ('Sally', 'May', 'smay@gmail.com'))
    # cur.execute("INSERT INTO tbl_persons(col_fname, col_lname, col_email) VALUES (?, ?, ?)", \
    #     ('Kevin', 'Bacon', 'kbacon@gmail.com'))
conn.close()

conn.commit()

print(conn.total_changes)

conn = sqlite3.connect("test.db")

with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_fname, col_lname, col_email FROM tbl_persons WHERE col_fname = 'Sarah'")
    # Fetchall() will retrieve the data that is pulled from the SELECT statement
    varPerson = cur.fetchall()
    for item in varPerson:
        msg = 'First Name: {}\nLast Name: {}\nEmail: {}'.format(item[0], item[1], item[2])
    print(msg)


conn.close()