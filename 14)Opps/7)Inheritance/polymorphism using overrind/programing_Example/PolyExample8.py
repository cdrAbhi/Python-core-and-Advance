#Polymorphism Prog
#PolyExample8.py
class Circle:
	def  __init__(self): # Original Constructor
		print("Drawing  Circle")

class Square(Circle):
	def __init__(self): # Overridden Constructor
		print("Drawing Square")
		super().__init__()

class Rect(Square):
	def __init__(self): # Overridden Constructor
		print("Drawing Rect")
		super().__init__()

#main program
r=Rect() # Object creation

