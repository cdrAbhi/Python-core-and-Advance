#Program for Demonstrating Instance Methods
#InstanceMethodEx3.py
class Sum:
	def readvalues(self):
		self.a=float(input("Enter First Value:"))
		self.b=float(input("Enter Second Value:"))
	def addop(self):
		self.c=self.a+self.b
	def disp(self):
		self.readvalues()
		self.addop()
		print("Val of a=",self.a)
		print("Val of b=",self.b)
		print("sum=",self.c)

#main program
so=Sum()
so.disp()
