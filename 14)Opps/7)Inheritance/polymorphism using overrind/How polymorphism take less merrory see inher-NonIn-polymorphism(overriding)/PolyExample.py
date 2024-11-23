#Polymorphism Prog
#PolyExample.py
class Circle:
	def  draw(self): # Original Method
		print("Drawing  Circle")
class Rect(Circle):
	def draw(self): # Overridden Method
		print("Drawing Rect")
		super().draw()
	
class Square(Rect):
	def  draw(self):# Overridden Method
		print("Drwing Square:")
		super().draw() # super() is used for calling Base Class Method from Derived Class Method
		
		
#main program
s=Square()
s.draw()
