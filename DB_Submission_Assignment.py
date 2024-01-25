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

for x in files:
    with conn:
        cur = conn.cursor()
        sql = "INSERT INTO tbl_files (col_fileName) VALUES (?)"
        
        cur.execute(sql, files[x])

# for i in tempTuple: 
#     with conn:
#         f = tempTuple(i)
#         cur = conn.cursor()
#         cur.execute("INSERT INTO tbl_files(col_fileName) VALUES (?)", \
#             (f))
#         conn.commit()

# for x in range(tempTuple): 
#     # temp = tempTuple[x]
#     with conn:
#         cur = conn.cursor()
#         sql = "INSERT INTO tbl_files (col_fileName) VALUES (?)"
#         temp = files[x]
#         cur.execute(sql, temp)


print(conn.total_changes)
conn.close()