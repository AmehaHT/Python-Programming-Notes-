class Particle:
    def __init__(self,n="",c=0):
        print("particle constructor")
    def __str__(self):
        return self.name +", "+str(self.charge) + '\n'
    
class Electron(Particle):
    def __init__(self,n,c):
        print("electron constructor")
        Particle.__init__(self,n,c)
    def __str__(self):
        return str("electrons: "+Particle.__str__(self))
        
class Proton(Particle):
    def __init__(self,n,c):
        print("proton constructor")
        super().__init__(n,c)
    def __str__(self):
        return str("protons: "+Particle.__str__(self))

class Neutron(Particle):    
    def __init__(self,n,c):
        print("neutron constructor")
        Particle.__init__(n,c)
    def __str__(self):
        return str("neutrons: "+Particle.__str__(self))

class Nucleus (Proton,Neutron):
    def __init__(self,n):
        print("nuculus constructor")
        Proton.__init__(self,n,1)
        Neutron.__init__(self,n,0)
    def __str__(self):
        return str(Proton.__str__(self)+Neutron.__str__(self))

class Atom(Nucleus,Electron): 
    def __init__(self,n,e):
        print("atom constructor")
        Nucleus.__init__(self,n)
        Electron.__init__(self,n,e)
        self.name = n
        self.charge = e
    def __str__(self):
        return str(Nucleus.__str__(self)+Electron.__str__(self))
        
class Animal:
    def __init__(self,name):
        print("animal constructor")
        self.name = name
    def speak(self):
        print("beep")

class Dog(Animal):
    def __init__(self,name):
        print("dog constructor")
        super().__init__(name)
    def speak(self):
        print("bark")

class Cat(Animal):
    def __init__(self,name):
        print("cat constructor")
        super().__init__(name)
    def speak(self):
        print("meow")
        
class Cheese:
    def __init__(self):
        self.fat = 100
        self.salt = 100
    def __str__(self):
        return " Cheese"

class Bacon:
    def __init__(self):
        self.deadpig = 0.10
    def __str__(self):
        return " Bacon"

class Hamburger:
    def __init__(self):
        self.deadcow = 0.25
        self.bun = 1.0
    def __str__(self):
        return "Hamburger: beef "+str(self.deadcow)+"\tBun "+str(self.bun)

class CheeseBurger( Hamburger ):
    def __init__(self):
        super().__init__()
        self.cheese = Cheese()
    def __str__(self):
        return str(Hamburger.__str__(self)) + str(self.cheese)
        
class BaconBurger( Hamburger ):
    def __init__(self):
        super().__init__()
        self.bacon = Bacon()
    def __str__(self):
        return str(Hamburger.__str__(self)) + str(self.bacon)

      
class Parent:        # define parent class
    def __init__(self):
        print ("parent constructor")
        self.parentAttr = 0
    def parentMethod(self):
        print ('parentmethod')
    def setAttr(self, attr):
        self.parentAttr = attr
        print ('parentsetAttr ',attr)
    def getAttr(self):
        print("parentattribute :", self.parentAttr)
      
class Child(Parent): # define child class
    def __init__(self):
        super().__init__()
        print("child constructor")
    def childMethod(self):
        print('hildmethod')

def Animals():
    animal = Animal("Unicorn")
    animal.speak()
    dog = Dog("Chihuahua")
    dog.speak()
    cat = Cat("Tabby")
    cat.speak()

def ParentChild():   
    parent = Parent()   #instance of parent
    parent.parentMethod()   # calls parent's method
    parent.setAttr(200)       # again call parent's method
    parent.getAttr()          # again call parent's method
    child = Child()          # instance of child
    child.childMethod()      # child calls its method
    child.parentMethod()     # calls parent's method
    child.setAttr(200)       # again call parent's method
    child.getAttr()          # again call parent's method

def Atoms():
    carbon = Atom("Carbon",6)
    print(carbon)
    
def Burger():
    cheeseburger = CheeseBurger()
    baconburger = BaconBurger()
    print(cheeseburger)
    print(baconburger)

def main():
    ParentChild()
    print(25*'=')
    Animals()
    print(25*'=')
    Atoms()
    print(25*'=')
    Burger()

main()


   
