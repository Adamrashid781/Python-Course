

class User:
    # Must add attributes here for the class
    name = 'No name provided'
    email = 'None'
    password = '1234abcd'
    account = 0 
    
    # define the class methods 
    
    def __init__(self, name, email, password, account):
        self.name = name
        self.email = email
        self.password = password
        self.account = account
    def login(self):
        entry_email = input('Enter your email: ')
        entry_password = input('Enter your password: ')
        if (entry_email == self.email and entry_password == self.password):
            print('Welcome back, {}'.format(self.name))
        else: 
            print('You are not authorized on this page.')
    
    

# Child classes of class User
class Employee(User):
    base_pay = 11.00
    department = 'General'

class Customer(User):
    mailing_address = ' '
    mailing_list = True 


# outside of the class you would create an instance of this page
new_user = User('John Doe', 'jdoe@outlook.com', 'p@ssword', 1234)

# Call the login method using the new object
new_user.login()