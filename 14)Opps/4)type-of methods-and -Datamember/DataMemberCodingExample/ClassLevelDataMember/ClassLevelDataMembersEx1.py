#Program for Demonstrating Class Level Data Members
#ClassLevelDataMembersEx1.py
class Student:
    crs="PYTHON"  # here crs is called Class Level Data Member

#main program
s1=Student()
s2=Student()
print("Initial Content of s1=",s1.__dict__)
print("Initial Content of s1=",s1.__dict__)
print("First Student s1 Course=",Student.crs)
print("Second Student s2 Course=",Student.crs)
# Here we are accessing Class Level Data members w.r.t Class Name



