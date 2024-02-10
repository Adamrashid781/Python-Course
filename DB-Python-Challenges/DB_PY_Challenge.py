
import sqlite3 



# Creating a DB in the RAM and giving it a name 
# conn = sqlite3.connect("':memory:' AS Roster")
conn = sqlite3.connect(':memory:')

c = conn.cursor()
# Creating table roster
c.execute("""CREATE TABLE if not exists tbl_roster(col_name TEXT, col_species TEXT, col_iq INT)""")
values = (('Jean-Baptiste Zorg', 'Human', 122), ('Korben Dallas', 'Meat Popsical', 100), ("Ak'not", 'Mangalore', -5))
c.executemany('INSERT INTO tbl_roster VALUES(?, ?, ?)', values)

# This block of code will print the data thats in the DB on the heap
c.execute('SELECT * FROM tbl_roster')
while True:
    row = c.fetchone()
    if row is None:
        break
    print(row)

c.execute("UPDATE tbl_roster SET col_species = 'Human' WHERE col_name = 'Korben Dallas' ")

# This block of code will print the data thats in the DB on the heap
c.execute('SELECT * FROM tbl_roster')
while True:
    row = c.fetchone()
    if row is None:
        break
    print(row)


print("\n\nWe will now display the names and IQ's of the people who are classified as Humanoids")
c.execute("SELECT col_name, col_iq FROM tbl_roster WHERE col_species = 'Human'")
while True:
    row = c.fetchone() 
    if row is None:
        break
    print(row)

conn.close()

