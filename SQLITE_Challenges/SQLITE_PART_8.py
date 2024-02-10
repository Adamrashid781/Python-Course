import sqlite3 

conn = sqlite3.connect('../Github/Python-Course/SQLITE_Challenges/Test_database.db')

c = conn.cursor()

c.execute("SELECT FirstName, LastName FROM People WHERE Age < 20")
while True:
    row = c.fetchone() 
    if row is None:
        break
    print(row)