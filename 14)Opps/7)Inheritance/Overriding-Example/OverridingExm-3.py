class Dog:
    def noise(self):
        print("Dog make noise Bow BOw")
        
class Cat(Dog):
    def noise(self):
       print("Cat noise Mauw Mauw")
        
class Cow(Cat):
    def noise(self):   
        super().noise() # use to call super class instance method
        Dog.noise(self)   #use to access specific instance method
        print("Cow noise Amba Amba=")

Animal=Cow()
Animal.noise()

# Note if you want to access and print specific super class instance method for inherit subclass use  Dog.noise(self)
'''
====Output=========

Cat noise Mauw Mauw
Dog make noise Bow BOw


** Process exited - Return Code: 0 **
Press Enter to exit terminal
'''