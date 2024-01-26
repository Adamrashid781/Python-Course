

class Game:
    var1 = 'Hello'
    var2 = 'World'


# This will be a parent class
class Organism:
    name = 'Unknown'
    species = 'Unknown'
    legs = None 
    arms = None
    dna = 'Sequence A'
    origin = 'Unknown'
    carbon_based = True 
    
    def information(self): 
        msg = '\nName: {}\nSpecies: {}\nLegs: {}\nArms: {}\nDNA: {}\nOrigin: {}\nCarbon Based: {}'.format(self.name, self.species, \
            self.legs, self.arms, self.dna, self.origin, self.carbon_based)
        return msg

# Child class instance
class Human(Organism):
    name = 'MacGuyver'
    species = 'Homosapiens'
    legs = 2
    arms = 2
    origin = 'Earth'
    
    def ingenuity(self):
        msg = '\nCreate a deadly weapon using only a paperclip, chewing gum, and a roll of duct dape!'
        return msg 
    
# Another child class 
class Dog(Organism):
    name = 'Spot'
    species = 'Canine'
    legs = 4
    arms = 0 
    dna = 'Sequence B'
    origin = 'Earth'
    
    def bite(self):
        msg = '\nEmits a loud, menacing growl and bites down ferociously on it''s target!'
        return msg 

# Another child class instance 
class Bacteria(Organism):
    name = 'X'
    species = 'Bacteria'
    legs = 0
    arms = 0
    dna = 'Sequence C'
    origin = 'Mars'
    
    def replication(self):
        msg = '\nThe cells begin to divide and multiple into new organisms'
        return msg 

# My own class for page 242 
class Mine:
    name = '' 
    age = ''
    work = ''
    
    def __init__(self, name, age, work):
        self.name = 'John Doe'
        self.age = '70'
        self.work = 'Janitor'
    
    def info(self):
        msg = '\nHello, my name is {}, and I am {} Years Old. I also work as a {}'.format(self.name, self.age, self.work)
        return msg

class Yours(Mine):
    pass


if __name__ == '__main__':
    x = Game()
    print('{} {}'.format(x.var1, x.var2))
    human = Human()
    dog = Dog()
    bacteria = Bacteria()
    me = Mine('', '', '')
    you = Yours('', '', '')
    
    print(human.information())
    print(human.ingenuity())
    
    print(dog.information())
    print(dog.bite())
    
    print(bacteria.information())
    print(bacteria.replication())
    
    print(me.info())
    print(you.info())
    