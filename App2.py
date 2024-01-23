
# importing app.py file for the function 

import App

def print_app2():
    name = (__name__)
    return name 

# print(print_app2())
if __name__ == '__main__':
    # the following is calling code from within this script
    print('I am running code from {}'.format(print_app2()))
    
    # the following is calling code from the imported App.py
    print('I am running code from {}'.format(App.print_app()))