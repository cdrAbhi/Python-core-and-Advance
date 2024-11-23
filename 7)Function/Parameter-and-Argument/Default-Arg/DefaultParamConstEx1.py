#Program for Demonstrating both Default and Parameterized  Constructors
#DefaultParamConstEx1.py
class Test:
	def  __init__(self,k=1,v=2): # Default / Parameterized Constructor
		print("---------------------------------")
		print("I am from Default Parameterized Constructor")
		print("---------------------------------")
		self.a=k
		self.b=v
		print("Val of a={}".format(self.a))
		print("Val of b={}".format(self.b))
		print("---------------------------------")

#main program
t1=Test() #Default  Constructor
t2=Test(100,200) # Parametrized Constructors
t3=Test(1000,2000) # Parametrized Constructors
t4=Test(500) # Parametrized Constructors
t5=Test(v=500) # Parametrized Constructors
t6=Test(v=-1,k=-2) # Parametrized Constructors


