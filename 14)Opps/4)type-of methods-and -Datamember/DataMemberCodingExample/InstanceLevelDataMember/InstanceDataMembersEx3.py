#program for Demonstarting Instance Data Members
#InstanceDataMembersEx3.py
class Sum:pass

#main program
s=Sum()
print("Intial Content of s1=",s.__dict__) # {}
#Add the Data to s
s.a=10
s.b=20
print(" Content of s1=",s.__dict__) # {'a': 10, 'b': 20}
s.c=s.a+s.b
print(" Content of s1=",s.__dict__) #  {'a': 10, 'b': 20, 'c': 30}
print("sum=",s.c)