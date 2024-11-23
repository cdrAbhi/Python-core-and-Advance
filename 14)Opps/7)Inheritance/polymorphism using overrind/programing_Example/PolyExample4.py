#Program for cal area of Different Figures
#PolyExample4.py
class Circle(object):
	def   area(self,r): # Original Method
		self.ac=3.14*r**2
		print("Area of Circle={}".format(self.ac))
	
class Square(Circle):
	def area(self,s):#Overridden Method
		self.sa=s**2
		print("Area of Square={}".format(self.sa))
		print("----------------------------------------------")
		super().area(float(input("Enter Radius:")))
	
class Rect(Square):
	def area(self,L,B):#Overridden Method
		self.ra=L*B
		print("Area of Rect={}".format(self.ra))
		print("----------------------------------------------")
		super().area(float(input("Enter Side:")))

	
#Main program
r=Rect()
r.area(float(input("Enter Length:")),float(input("Enter Breadth:")) )

