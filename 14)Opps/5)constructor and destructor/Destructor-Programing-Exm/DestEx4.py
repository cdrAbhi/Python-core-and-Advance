#Program for Demonstrating Destructors
#DestEx4.py
import time
class Employee:
	def  __init__(self,eno,ename): # Parameterized Constructor
		print("-"*30)
		print("I am from Parameterized Constructor")
		self.eno=eno
		self.ename=ename
		print("\tEmp Number:{}".format(self.eno))
		print("\tEmp Name:{}".format(self.ename))
		print("-"*30)

	def __del__(self):  # Destructor Def...
		print("GC Calls __del__(self)--for de-allocating memory space")

#main progran
print("Program Execution  Started")
eo1=Employee(100,"RS") # Object Creation--Makes PVM to Call Parameterized Constructor
print("No Longer Intereted to maintain memory space of eo1")
time.sleep(3)
del eo1  # Calling Destructor by GC Forcefully
eo2=Employee(200,"TS") # Object Creation--Makes PVM to Call Parameterized Constructor
print("No Longer Intereted to maintain memory space of eo2")
time.sleep(3)
del eo2  # Calling Destructor by GC Forcefully
eo3=Employee(300,"DR") # Object Creation--Makes PVM to Call Parameterized Constructor
print("No Longer Intereted to maintain memory space of eo2")
time.sleep(3)
del eo3  # Calling Destructor by GC Forcefully
print("Program Execution  Ended")
time.sleep(3)