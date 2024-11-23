#Program for Demonstrating Static Methods
#StaticMethodEx3.py
class Student:
	def  getstudvals(self):
		self.sno=int(input("Enter Student Number:"))
		self.sname=input("Enter Student Name:")
		self.marks=float(input("Enter Student Marks:"))
	
class Employee:
	def  getempvals(self):
		self.eno=int(input("\nEnter Employee Number:"))
		self.ename=input("Enter Employee Name:")

		
class Teacher:
	def  getteachervals(self):
		self.tno=int(input("\nEnter Teacher Number:"))
		self.tname=input("Enter Teacher Name:")
		self.subject=input("Enter Teacher Subject:")
		self.expe=int(input("Enter Teacher Experience:"))

class Hyd:
	@staticmethod
	def dispobjectdata( objdata,objinfo ):
		print("*"*50)
		print("'{}' Information".format(objinfo))
		print("*"*50)
		for dmn,dmv in objdata.__dict__.items():
			print("\t{}--->{}".format(dmn,dmv))
		print("*"*50)
	
#main progran
s=Student()
e=Employee()
t=Teacher()
s.getstudvals()
e.getempvals()
t.getteachervals()
#I want to display any type of object content --we need a method--Universal Operation--static method
Hyd().dispobjectdata(s,"Student") # static method accessed w.r.t. Name-Less Object
Hyd().dispobjectdata(e,"Employee") # static method accessed w.r.t. Name-Less Object 
Hyd().dispobjectdata(t,"Teacher")  # static method accessed w.r.t. Name-less Object