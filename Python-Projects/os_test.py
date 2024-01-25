import os 

# This file is on adding data to a file and reading that data

print(os.getcwd())

# print(help(open))

def writeData():
    data = input('What would you like to add to the file? \n>>>')
    
    with open('../Python-Course/test/test.txt', 'a') as f:
        f.write('\n' + data)
        f.close



def openFile():
    with open('../Python-Course/test/test.txt', 'r') as f:
        data = f.read()
        print(data)
        f.close



if __name__ == '__main__':
    openFile()
    writeData()
    openFile()