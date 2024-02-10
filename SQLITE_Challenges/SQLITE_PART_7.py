import sqlite3 

peopleValues = (('Ron', 'Obvious', 42), ('Luigi', 'Vercotti', 43), ('Arthir', 'Belling', 28))

with sqlite3.connect('../Github/Python-Course/SQLITE_Challenges/Test_database.db') as connection:
    c = connection.cursor() 
    c.execute("DROP TABLE IF EXISTS People")
    c.execute("CREATE TABLE People(FirstName TEXT, Lastname TEXT, Age INT)")
    c.executemany("INSERT INTO People VALUES(?, ?, ?)", 
                  peopleValues)
    
    # Select all first and last names from people over age of 30 
    c.execute("SELECT FirstName, LastName FROM People WHERE Age > 30")
    for row in c.fetchall():
        print(row)