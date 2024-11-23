#Program for Demonstrating Instance Methods
#InstanceMethodEx1.py
class Student:
	def  readstudvalues(self,objinfo):
		self.sno=int(input("Enter {} Student Number:".format(objinfo)))
		self.sname=input("Enter {} Student Name:".format(objinfo))
		self.marks=float(input("Enter {} Student Marks:".format(objinfo)))
	
	def dispstuddata(self,objinfo):
		print("{} Student Information".format(objinfo))
		print("-"*50)
		print("Student Number:{}".format(self.sno))
		print("Student Name:{}".format(self.sname))
		print("Student Marks:{}".format(self.marks))
		print("-"*50)

#main program
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
#display s1 object data
s1.dispstuddata("First") #   # Method Call
#display s2 object data
s2.dispstuddata("Second")   # Method Call