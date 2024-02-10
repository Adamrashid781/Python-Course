import sqlite3

connection = sqlite3.connect('../Github/Python-Course/SQLITE_Challenges/Test_database.db')

# TO CREATE A TEMPORARY DATABASE IN THE RAM, USE ':memory:' INSTEAD OF A DATABASE NAME
# connection = sqlite3.connect(':memory:')


c = connection.cursor()

c.execute('CREATE TABLE if not exists People(FirstName TEXT, LasName TEXT, Age INT)')

c.execute("INSERT INTO People VALUES('Ron', 'Obvious', 42)")
connection.commit()

# with sqlite3.connect("Test_database.db") as connection:
with connection as conn:
    # c = conn.cursor()
    c.executescript("""DROP TABLE IF EXISTS People; 
        CREATE TABLE People(FirstName TEXT, LastName TEXT, AGE INT) ; 
        INSERT INTO People VALUES('Ron', 'Obvious', '43')""")
    
    
    # We can use the "executemany" command to send it many bits of data at a time
    # The data must be written as a tuple of tuples 
    peopleValues = (('Luigi', 'Vercotti', 43), ('Arthur', 'Belling', 28))
    c.executemany("INSERT INTO People VALUES(?, ?, ?)", peopleValues)
    print(peopleValues)
    connection.commit()



# MUST ALWAYS CLOSE THE CONNECTION WHEN WE'RE DONE
c.close() 