#Program for cal area of Different Figures
#PolyExample5.py
class Circle(object):
	def   area(self,r): # Original Method
		self.ac=3.14*r**2
		print("Area of Circle={}".format(self.ac))
	
class Square(Circle):
	def area(self,s):#Overridden Method
		self.sa=s**2
		print("Area of Square={}".format(self.sa))
		

class Rect(Square):
	def area(self,L,B):#Overridden Method
		self.ra=L*B
		print("Area of Rect={}".format(self.ra))
		print("----------------------------------------------")
		Circle.area(self,float(input("Enter Radius:")))
		print("----------------------------------------------")
		Square.area(self,float(input("Enter Side:")))

	
#Main program
r=Rect()
r.area(float(input("Enter Length:")),float(input("Enter Breadth:")) )

