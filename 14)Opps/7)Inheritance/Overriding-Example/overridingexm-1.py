class Dog:
    def noise(self):
        print("Dog make noise Bow BOw")
class Cat(Dog):
    def noise(self):
       print("Cat noise Mauw Mauw")
        

Animal=Cat()
Animal.noise()

# Note: Derive and Base class having a instance method with same then Derive class instance method overide Base class instance method. 