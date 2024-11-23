#Polymorphism Prog
#PolyExample9.py
class Circle:
	def  __init__(self): # Original Constructor
		print("Drawing  Circle")

class Square(Circle):
	def __init__(self): # Overridden Constructor
		print("Drawing Square")

class Rect(Square):
	def __init__(self): # Overridden Constructor
		print("Drawing Rect")
		Circle.__init__(self)
		Square.__init__(self)

#main program
r=Rect() # Object creation

