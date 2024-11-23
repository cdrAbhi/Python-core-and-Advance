#Program for Demonstrating Static Methods
#StaticMethodEx7.py
class Student:
	def  getstudvals(self):
		self.sno=int(input("Enter Student Number:"))
		self.sname=input("Enter Student Name:")
		self.marks=float(input("Enter Student Marks:"))
		#call static method of Hyd class from Instance method of Student Class
		Hyd. dispobjectdata( self, "Student")

	
class Employee:
	def  getempvals(self):
		self.eno=int(input("\nEnter Employee Number:"))
		self.ename=input("Enter Employee Name:")
		#call static method of Hyd class from Instance method of Employee Class
		Hyd. dispobjectdata( self, "Employee")

class Teacher:
	def  getteachervals(self):
		self.tno=int(input("\nEnter Teacher Number:"))
		self.tname=input("Enter Teacher Name:")
		self.subject=input("Enter Teacher Subject:")
		self.expe=int(input("Enter Teacher Experience:"))
		#call static method of Hyd class from Instance method of Teacher Class
		Hyd. dispobjectdata( self, "Teacher")

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

