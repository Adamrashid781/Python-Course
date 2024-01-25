import os 
# print(os.getcwd())


# this is how we will create an absolute path for a file in the OS

fName = 'Hello.txt'

fPath = '/Users/adam/Desktop/GitHub/Python-Course'

# Syntax - os.path.join(path, fileName)
abPath = os.path.join (fPath, fName)
print(abPath)