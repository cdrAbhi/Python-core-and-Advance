#Program for cal area of Different Figures
#PolyExample7.py
class Circle:
	def   area(self,r): # Original Method
		self.ac=3.14*r**2
		print("Area of Circle={}".format(self.ac))
class Square:
	def area(self,s):#Original Method
		self.sa=s**2
		print("Area of Square={}".format(self.sa))
		
class Rect(Circle,Square):
	def area(self,L,B): # Overridden Method
		self.ar=L*B
		print("Area of Rect={}".format(self.ar))
		print("--------------------------------------------------")
		Square.area(self,float(input("Enter Side:")))
		print("--------------------------------------------------")
		Circle.area(self,float(input("Enter Radius:")))
	
#Main program
r=Rect()
r.area(float(input("Enter Length:")),float(input("Enter Breadth:")))


