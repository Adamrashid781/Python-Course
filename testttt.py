a = 5**2; 
print(a) 

Stupid = 'Hello, World'
print(Stupid)

print(len(Stupid))

print(Stupid[3])

fName = 'Sadam'
lName = 'Rashid'
print(fName + ' ' + lName)

# the curly brackets will hold the space of a variable by using the .format
print('Hello {} {}, welcome to python!'.format(fName, lName))


# Python challenges

# mulitline string 
long_string = '''   This is going to be a multi line srting.
                    With new lines and tabs and yeah'''  
print(long_string)

print(long_string[3], long_string[8], long_string[12])
print(len(long_string))
print(long_string.strip())
print(long_string.upper())
x = 'This'
print(x  in long_string)
print(x  not in long_string)

print(fName + ' ' + lName)
print(' this is the escape key in action: it\'s')


num1 = 1.3
num2 = 2
print(num1 + num2 )

# operators challenge 
# arithmatic + assignment opperator 
num1 += num2

# Comparison operator
if num1 > num2 :
    print('num1 is greater than num2')

# logical operator 
if num1 > num2 and num1 < 4: 
    print('num1 is greater than num2 and greater than 4')

# Identity operator     
if num1 is x: 
    print('num1 and x are the same data type')
    
else: 
    print('they are not the same data type')
    
# membership operator 
x = 'This'
print(x  in long_string)
print(x  not in long_string)

# Bitwise operator 
read_permission = 4
write_permission = 2
execute_permission = 1

permissions = read_permission | write_permission # 4 + 2 = 6
permissions |= execute_permission      # 6 + 1 = 7

print(permissions)
print(bin(permissions))
# this shifts the binary number over to the left by the value of the second digit in the ()
# 0000 0001 will be a 0000 0010 after a one place shift to the left
print(1 << 1)


animal = ('zebra', 'lion', 'aligator', 'goat', 'giraffe', 'ox')
listOfAnimals = list(animal)
print(listOfAnimals)
print(animal)

listOfAnimals.append ('honey badger')
print(listOfAnimals)
myString = 'I am trying to use a load of new extensions for Python. but they are kinda confusing'
print(len(myString))
newString = list(myString)
print(newString)

print(7 + 10)
ran = listOfAnimals.copy()
print(newString  + ran)

print(ran.reverse())

for i in list(animal):
    print(i)

print(myString.count('a'))


myset = {'baseball', 'soccer', 'basketball'}
myset.add('UFC')
print(myset)
myset.remove('soccer')
print(myset)

set2 = {'baseball', 'soccer', 'basketball', 'hockey', 'water polo'}
print(set2.difference(myset))

myDictionary = {'index0': 1, 'index1':2, 'index2': 3}
print(myDictionary['index2'])
print(myDictionary.get('index0'))
dic_users = {'emp_2': myDictionary, 'emp_3': {'fname': 'Bob', 'lname': 'Smith', 'phone': '123-456-7890'}}
print(dic_users['emp_2'])
print(dic_users['emp_3'])
print('user: {} {}\nPhone: {}'.format(dic_users['emp_3']['fname'], dic_users['emp_3']['lname'], dic_users['emp_3']['phone']))


thisdict = ('key1', 'key2', 'key3')
print(dict.fromkeys(thisdict, 3))
print(type(myString))

boolean_var = True 

if a != 15:
    if boolean_var:
        print('A is equal to 25')
    elif a != 25:
        print('A is not equal to 25')
else: 
    print('Boolean_var = False, and A does not equal 25')

bz = bool(1)
if bz: 
    print('BZ bool is true')
else: 
    print('BZ bool is false')

dr = 'z'
dc = isinstance(dr, str)
print(dc)


i = 0
for i in range(10):
    print(' {} iteration through the loop'.format(i))
    
    i += 1
    if i == 8:
        print('breaking out of the for loop')
        break
    else:
        continue 

i = 0


while i < 10:
    print(' {} iteration through the loo0p'.format(i))
    i += 1
    if i == 5:
        print('Breaking out of the while loop')
        break
    else: 
        print('continuing ')
        continue
i = 0


name = 'Python'
print(len(name))
for i in enumerate(name):
    print(i)