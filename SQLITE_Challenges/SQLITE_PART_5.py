import sqlite3 

# Get personal data from user 
firstName = input('Enter your first name: ')
lastName = input('Enter your last name: ')
age = int(input('Enter your age: '))

# Execute insert statement for the supplied person data 
with sqlite3.connect('../Github/Python-Course/SQLITE_Challenges/Test_database.db') as connection:
    c = connection.cursor()
    
    c.execute("""CREATE TABLE if not exists People(firstName TEXT, lastName TEXT, Age INT)""")
    
    line = "INSERT INTO People VALUES('" + firstName + "', '" + lastName + "', " + str(age) + ")"
    
    # line = "INSERT INTO People VALUES('Flanery', 'O''Connor', 22 )" 
    
    
    print(line)
    c.execute(line)