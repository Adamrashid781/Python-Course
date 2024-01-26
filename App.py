
# this file is considered a module because it is a file with a 
# function in it that can be called in another file (app2.py)

# Dunder means Double Underline 
# __main__ 

# this function will not run until a file calls the function 
def print_app():
    name = (__name__)
    return name

print(print_app())

if __name__ == '__main__':
    print('I am in main')
else:
    print('I am in secondary file')