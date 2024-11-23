#Program for Demonstrating Inheritance
#InhProg1.py
class BC:
	def  getA(self):
		self.a=10

class DC(BC):   # Single  Inheritance
	def  getB(self):
		self.b=20

#main program
do1=DC()
print("Content of do1=",do1.__dict__) # {}
do1.getA()
print("Content of do1=",do1.__dict__) # {'a':10}
do1.getB()
print("Content of do1=",do1.__dict__) # {'a':10,'b':20}