#Program for cal area of Different Figures
#PolyExample3.py
class Circle(object):
	def   area(self): # Original Method
		self.r=float(input("Enter Radius:"))
		self.ac=3.14*self.r**2
		print("Area of Circle={}".format(self.ac))

class Square(Circle):
	def area(self):#Overridden Method
		self.s=float(input("Enter Side:"))
		self.sa=self.s**2
		print("Area of Square={}".format(self.sa))

class Rect(Square):
	def area(self):#Overridden Method
		self.l=float(input("Enter Length:"))
		self.b=float(input("Enter Breadth:"))
		self.ra=self.l*self.b
		print("Area of Rect={}".format(self.ra))
		print("---------------------------------------------------")
		Circle.area(self)
		print("---------------------------------------------------")
		Square.area(self)

#Main program
r=Rect()
r.area()

