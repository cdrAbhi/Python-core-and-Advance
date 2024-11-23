#Program for Demonstrating Class Level Methods
#ClassLevelMethodEx1.py
class Student:
	@classmethod
	def  getcrs(cls):  # Class Level Method
		cls.crs="PYTHON"
		Student.city="HYD" # Here crs and city are called Class Level Data Members

	def  readstudvalues(self,objinfo):  # Instance Method
		self.sno=int(input("Enter {} Student Number:".format(objinfo)))
		self.sname=input("Enter {} Student Name:".format(objinfo))
		self.marks=float(input("Enter {} Student Marks:".format(objinfo)))
	
	def dispstuddata(self,objinfo):  # Instance Method
		print("{} Student Information".format(objinfo))
		print("-"*50)
		print("Student Number:{}".format(self.sno))
		print("Student Name:{}".format(self.sname))
		print("Student Marks:{}".format(self.marks))
		print("STUDENT COURSE:{}".format(Student.crs))
		print("STUDENT CITY:{}".format(Student.city))
		print("-"*50)

#Main Program
s1=Student()  # Object Creation
s2=Student()  # Object Creation
print("*"*50)
print("ID of s1=",id(s1))
print("ID of s2=",id(s2))
print("*"*50)
#read the Instance data for s1
s1.readstudvalues("First")  # Method Call
print("-"*40)
#read the Instance data for s2
s2.readstudvalues("Second")  # Method Call
#call Class Level Method w.r.t Class Name
Student.getcrs()
#display s1 object data
s1.dispstuddata("First") #   # Method Call
#display s2 object data
s2.dispstuddata("Second")   # Method Call

