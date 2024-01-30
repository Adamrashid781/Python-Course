

class Parent:
    var1 = 'Fayeq'
    var2 = 'Rashid'
    
    def print_info(self):
        print('Hello, my name is {} {}'.format(self.var1, self.var2))

class Child1(Parent):
    # Date of Birth
    dob = '04/21/2001'
    parent_name = Parent.var1 + ' ' + Parent.var2
    
    def print_info(self):
        print('Hello, my dads name is {}, and I was born on {}'.format(self.parent_name, self.dob))

class Child2(Parent):
    var1 = 'Ayia'
    var2 = 'Rashid'
    
    def print_info(self):
        print('Hello, my name is {} {}'.format(self.var1, self.var2))


if __name__ == '__main__':
    parent = Parent()
    child1 = Child1()
    child2 = Child2()
    
    parent.print_info()
    child1.print_info()
    child2.print_info()
    
