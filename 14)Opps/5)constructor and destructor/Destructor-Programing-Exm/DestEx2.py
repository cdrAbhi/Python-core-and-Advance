#Program for Demonstrating Destructors
#DestEx2.py
import time,sys
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
		global totmem
		print("\tGC Calls __del__(self)--for de-allocating memory space")
		totmem=totmem-sys.getsizeof(self)
		print("\tAt Present Total Memory Space:{}".format(totmem))

#main progran
print("Program Execution  Started")
eo1=Employee(100,"RS") # Object Creation--Makes PVM to Call Parameterized Constructor
eo2=Employee(200,"TS") # Object Creation--Makes PVM to Call Parameterized Constructor
eo3=Employee(300,"DR") # Object Creation--Makes PVM to Call Parameterized Constructor
totmem=sys.getsizeof(eo1)+sys.getsizeof(eo2)+sys.getsizeof(eo3)
print("InitialTotal Memory Space of Currrent Program=",totmem) # 144
print("Program Execution  Ended")
time.sleep(10)

