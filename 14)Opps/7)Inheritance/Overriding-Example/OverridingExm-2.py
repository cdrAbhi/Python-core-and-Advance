class Dog:
    def noise(self):
        print("Dog make noise Bow BOw")

class Cat(Dog):
    def noise(self):
       print("Cat noise Mauw Mauw")
       super().noise()       #Use to call super class instance method
        


Animal=Cat()
Animal.noise()

# Note : Still if you want to use Base class same name instance method then use super() function
'''
===Output==============
Cat noise Mauw Mauw
Dog make noise Bow BOw


** Process exited - Return Code: 0 **
Press Enter to exit terminal
===================================
'''