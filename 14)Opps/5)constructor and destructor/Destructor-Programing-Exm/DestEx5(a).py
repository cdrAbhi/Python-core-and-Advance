#Program for Demonstrating Destructors
#DestEx5.py
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
eo1=Employee(100,"RS") # Object Creation--GC not Makes PVM to Call Parameterized Constructor ==>create a object
eo2=eo1 # refference to eo1 not deep copy--not Makes PVM to Call Parameterized Constructor ==>not create a object refference to object
eo3=eo1 # refference to eo1 not deep copy--not Makes PVM to Call Parameterized Constructor ==>not create a object refference to object
print("Program Execution  Ended")
time.sleep(5)

'''
Note:
======
so that's mean in above program only one object created so GC will call Destructer only once. 

'''



