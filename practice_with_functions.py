


def start():
    print(get_number())
    print('Hello {}!'.format(get_name()))


def get_number():
    number = 12
    return number

def get_name():
    name = input('What is your name?\n\t>>>')
    return name

def start1():
    f_name = 'Sarah'
    l_name = 'Connor'
    age = 28
    gender = 'Female'
    get_info(f_name, l_name, age, gender)

def get_info(f_name, l_name, age, gender):
    print('Hello, my name is {} {}, I am a {} year old {}'.format(f_name, l_name, age, gender))


if __name__ == "__main__":
    start() 
    start1()