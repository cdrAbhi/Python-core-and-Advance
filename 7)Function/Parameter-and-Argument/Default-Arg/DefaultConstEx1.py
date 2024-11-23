#Program for Demonstrating Default Constructor
#DefaultConstEx1.py
class Test:
	def  __init__(self): # Default Constructor
		print("---------------------------------")
		print("I am from default Constructor")
		print("---------------------------------")
		self.a=10
		self.b=20
		print("Val of a={}".format(self.a))
		print("Val of b={}".format(self.b))
		print("---------------------------------")

#Main Program
t1=Test() # Object Creation--want to Initlize with 10 and 20
t2=Test() # Object Creation--want to Initlize with 10 and 20
t3=Test() # Object Creation--want to Initlize with 10 and 20