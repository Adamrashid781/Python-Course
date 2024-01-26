import sqlite3

conn = sqlite3.connect('My.db')

fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'Data.pdf', 'myPhoto.jpg')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fileName STRING \
        )")
    conn.commit()


files = []


conn = sqlite3.connect('My.db')

for a in fileList:
    if a.endswith('.txt'):
        files.append(a)


print(files)


for i in files: 
    with conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO tbl_files(col_fileName) VALUES (?)", (i,))
        conn.commit()


print(conn.total_changes)
conn.close()