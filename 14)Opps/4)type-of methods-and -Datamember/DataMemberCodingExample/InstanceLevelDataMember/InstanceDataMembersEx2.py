#program for Demonstarting Instance Data Members
#InstanceDataMembersEx2.py
class Student:pass

#main program
s1=Student()  # Object Creation
s2=Student()  # Object Creation
print("Initial Content of Object s1={} and Number of Values={}".format(s1.__dict__, len(s1.__dict__)))
print("Initial Content of Object s2={} and Number of Values={}".format(s2.__dict__, len(s2.__dict__)))
#add Instance Data Members to object s1--through Object Name
s1.sno=100
s1.name="RS"
s1.marks=44.44 # here sno,name and marks are called Instance Data Members
#add Instance Data Members to object s2--through Object Name
s2.sid=200
s2.sname="TR"
s2.marks=55.55
print("*"*50)
print("Content of Object s1={} and Number of Values={}".format(s1.__dict__, len(s1.__dict__)))
print("Content of Object s2={} and Number of Values={}".format(s2.__dict__, len(s2.__dict__)))
print("*"*50)
print("First Student Information:")
print("*"*50)
for idm,idv in s1.__dict__.items():
    print("\t{}--->{}".format(idm,idv))
print("*"*50)
print("Second Student Information:")
print("*"*50)
for idm,idv in s2.__dict__.items():
    print("\t{}--->{}".format(idm,idv))
print("*"*50)






