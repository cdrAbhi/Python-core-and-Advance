#Program for cal area of Different Figures
#PolyExample10.py
class Circle:
	def   __init__(self,r): # Original Constructor
		self.ac=3.14*r**2
		print("Area of Circle={}".format(self.ac))
class Square:
	def __init__(self,s):#Original  Constructor
		self.sa=s**2
		print("Area of Square={}".format(self.sa))
		
class Rect(Circle,Square):
	def __init__(self,L,B): # Overridden Constructor
		self.ar=L*B
		print("Area of Rect={}".format(self.ar))
		print("--------------------------------------------------")
		Square.__init__(self,float(input("Enter Side:")))
		print("--------------------------------------------------")
		Circle.__init__(self,float(input("Enter Radius:")))
	
#Main program
r=Rect(float(input("Enter Length:")),float(input("Enter Breadth:")))



