

class One:
    # this is the protected variable, with one underscore
    _protectedvar1 = 12
    # This is the private var, with two underscores
    __privatevar1 = 22
    
    # this function will print our private variable
    def getPrivate(self):
        print(self.__privatevar1)




# here we are creating the object of class one 
obj = One()
# Here we are calling the function to print the private variable
obj.getPrivate() 
# Here we are just calling the protected variable in the print statement to view it 
print(obj._protectedvar1)