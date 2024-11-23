#Program for Demonstrating need of Constrctors
#Non-ConstEx1.py
class Student:
	def  readstduvals(self):
		self.sno=10
		self.sname="RS"

#Main Program
s=Student()
print("content of s=",s.__dict__)  #  { }
#place the Instance Data in object s
s.readstduvals() # Calling Instance Method Explicitly
print("content of s=",s.__dict__) # {'sno': 10, 'sname': 'RS'}