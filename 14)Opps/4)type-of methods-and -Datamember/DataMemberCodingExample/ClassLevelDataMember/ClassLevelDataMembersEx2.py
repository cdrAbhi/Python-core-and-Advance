#Program for Demonstrating Class Level Data Members
#ClassLevelDataMembersEx2.py
class Student:
    crs="PYTHON"  # here crs is called Class Level Data Member

#main program
s1=Student()
s2=Student()
print("Initial Content of s1=",s1.__dict__)
print("Initial Content of s1=",s1.__dict__)
print("-------------------------------------------------------")
print("First Student s1 Course=",s1.crs)
print("Second Student s2 Course=",s2.crs)
# Here we are accessing Class Level Data members w.r.t Object Name of Correspoding Class



