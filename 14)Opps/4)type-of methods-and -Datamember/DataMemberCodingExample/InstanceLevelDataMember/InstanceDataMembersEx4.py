#program for Demonstarting Instance Data Members
#InstanceDataMembersEx4.py
class Sum:pass

#main program
s=Sum()
print("Intial Content of s1=",s.__dict__) # {}
#Add the Data to s
s.a=float(input("Enter First Value:"))
s.b=float(input("Enter Second Value:"))
print(" Content of s1=",s.__dict__) # {'a': 10, 'b': 20}
s.c=s.a+s.b
print(" Content of s1=",s.__dict__) #  {'a': 10, 'b': 20, 'c': 30}
print("sum=",s.c)