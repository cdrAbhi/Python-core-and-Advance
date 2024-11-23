#Program for Demonstrating Destructors
#DestEx5.py
import copy,sys,time

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
		global memsize
		print("GC Calls __del__(self)--for de-allocating memory space of object")
		print(f"Current memory space Occupied by object is : {memsize-sys.getsizeof(self)} ")
		memsize-=sys.getsizeof(self)
		time.sleep(5)
		print("Program Execution  Ended" if memsize==0 else "Deallocation done !!!")

#main progran
print("Program Execution  Started")
eo1=Employee(100,"RS") # Object Creation--Makes PVM to Call Parameterized Constructor
eo2=copy.deepcopy(eo1) # Deep Copy
eo3=copy.deepcopy(eo1) # Deep Copy
memsize=sys.getsizeof(eo1)+sys.getsizeof(eo2)+sys.getsizeof(eo3)
print(f"Total memory space taken by object : {memsize} ")
time.sleep(5)




'''
Note: 
=====
Here we are doing deep copy of object eo1 to eo2 and eo3 that's mean we are creating three object eo1,eo2 and eo3 Hence GC call destructor three time.

'''