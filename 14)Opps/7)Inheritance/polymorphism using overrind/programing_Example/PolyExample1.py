#Polymorphism Prog
#PolyExample1.py
class Circle:
	def  draw(self): # Original Method
		print("Drawing  Circle")
class Rect(Circle):
	def draw(self): # Overridden Method
		print("Drawing Rect")
		
class Square(Rect):
	def  draw(self):# Overridden Method
		print("Drwing Square:")
		Circle.draw(self)		
		Rect.draw(self)
		
#main program
s=Square()
s.draw()
