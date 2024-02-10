import sqlite3 

# Get the personal data from the user an insert into a tuple 
firstName = input('Enter your first name: ')
lastName = input('Enter your last name: ')
age = int(input('Enter your age: '))
personData = (firstName, lastName, age)


# Execute insert statement for supplied person data 
with sqlite3.connect('../Github/Python-Course/Test_database.db') as connection:
    c = connection.cursor() 
    c.execute("INSERT INTO People VALUES(?, ?, ?)", personData)
    c.execute("UPDATE People SET Age = ? WHERE FirstName = ? AND LastName = ?", (45, 'Luigi', 'Vercotti'))
    c.commit()
    c.close()