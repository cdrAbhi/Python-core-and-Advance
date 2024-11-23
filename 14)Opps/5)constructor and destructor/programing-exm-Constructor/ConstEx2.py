#Program for Demonstrating need of Constrctors
#ConstEx2.py
class Student:
	def  __init__(self,sno,sname): # Parameterized Constructor 
		print("i am from Parameterized Constructor")
		self.sno=sno
		self.sname=sname
		

#Main Program
s1=Student(100,"RS") # Object Creation---PVM Call Parameterized Constructor 
print("Content of s1=",s1.__dict__)
s2=Student(200,"TR") # Object Creation---PVM Call Parameterized Constructor 
print("Content of s2=",s2.__dict__)
s3=Student(300,"SR") # Object Creation---PVM Call Parameterized Constructor 
print("Content of s3=",s3.__dict__)




