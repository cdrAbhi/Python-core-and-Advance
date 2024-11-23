#program for Demonstarting Instance Data Members
#InstanceDataMembersEx1.py
class Student:pass

#main program
s1=Student()  # Object Creation
s2=Student()  # Object Creation
print("------------------------------------")
print("Id of s1=",id(s1))
print("Id of s2=",id(s2))
print("------------------------------------")
#add Instance Data Members to object s1--through Object Name
s1.sno=100
s1.name="RS"
s1.marks=44.44 # here sno,name and marks are called Instance Data Members
#add Instance Data Members to object s2--through Object Name
s2.sid=200
s2.sname="TR"
s2.marks=55.55
print("*"*50)
print("First Student Information:")
print("*"*50)
print("Student Number={}".format(s1.sno))
print("Student Name={}".format(s1.name))
print("Student Marks={}".format(s1.marks))
#Here we are accessing Instance Data members by using Object Name
print("*"*50)
print("Second Student Information:")
print("*"*50)
print("Student Number={}".format(s2.sid))
print("Student Name={}".format(s2.sname))
print("Student Marks={}".format(s2.marks))
print("*"*50)
#Here we are accessing Instance Data members by using Object Name





