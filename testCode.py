import math 

mySentence = ' loves the color '

color_list = ['red', 'blue', 'green', 'pink', 'teal', 'black']

def color_function(name):
    lst = []
    for i in color_list:
        msg = '{}{}{}'.format(name, mySentence, i)
        lst.append(msg)
    return lst








def get_name():
    go = True
    while go:
        name = input('What is your name? ')
        if name == '':
            print('You need to provide your name! ')
        elif name == 'Sally':
            print('Sally, you are not wanted here. Go AWAY!')
        
        else:
            go = False
    lst = color_function(name)
    for i in lst:
        print(i)

# get_name()

def name():
    go = True
    
    while go:
        fname = input('what is your first name? ')
        if fname == '':
            print('You must put in your first name! ')
        else: go = False
    go = True 
    
    while go:
        lname = input('What is your last name? ')
        if lname == '':
            print('You must put in your last name! ')
        else: 
            go = False
    print('Hello {} {}, welcome to your awesome staycation'.format(fname, lname))

# name()


array = ['susu', 'adam', 'jon', 'kawthar', 'maysoon']

# for i in array:
    # print(i)

# print(array.count('adam'))
# array.sort(reverse = True)
# print(array)

y = lambda x: x * x * x
print(y(20))

# printing in Binary, using Format()
k = format(1000, 'b')
print(k)
# Printing in binary, hexadecimal, and percentage using Format()
print('binary: {0:b}, hexadecimal: {0:x}, percentage: {0:%}'.format(27) )



def getSum(num1, num2):
    ''' This is a docstring of the getSum function'''
    sum = num1 + num2
    print('The total Sum of both digits {} {}, is equal to: {}'.format(num1, num2, sum))
    return sum

var = getSum(2, 10)

print(getSum.__doc__)