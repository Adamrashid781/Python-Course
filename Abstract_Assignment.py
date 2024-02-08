from abc import ABC, abstractmethod


class Laptop(ABC):
    def cost(self, amount):
        print('Your laptop costs: ', amount)
    
    # Below, we are instantiating the abstract method
    @abstractmethod
    def payment(self, amount):
        pass 

class Cash(Laptop):
    def payment(self, amount):
        print('You want to purchase the laptop for: {}'.format(amount))



obj1 = Cash()
obj1.cost('200')
obj1.payment('200')