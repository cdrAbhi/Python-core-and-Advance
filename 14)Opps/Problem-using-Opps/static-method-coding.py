# write python program which will in which create classs of empolee,student and teacher and store data in form of instance data member and get data by using static method

class Employee:
    def empdata(self):
        self.name="Manish"
        self.company="TCS"
        self.id="Manish123"
        
        
class Student:
    def studata(self):
        self.name="Anand"
        self.id="Anand123"
        self.crs="Python"
class Teacher:
    def tchdata(self):
        self.name="Minakshi"
        self.sub="Java"
        self.id="Java123"
        
class data:
    def cdata(self):
        self.city="Patna"
        self.country="India"
    @staticmethod
    def udata(empobj,stdobj,tchobj,cobj):
        print("Employee data : ",empobj.__dict__)
        print("Student data : ",stdobj.__dict__)
        print("Teacher data : ",tchobj.__dict__)
        print("Common data : ",cobj.__dict__)
emp=Employee()
std=Student()
tch=Teacher()
emp.empdata()
std.studata()
tch.tchdata()
d=data()
d.cdata()
d.udata(emp,std,tch,d)
# print(f"Employee data : {emp.__dict__}")
# print(f"Student data : {std.__dict__}")
# print(f"Teacher data : {tch.__dict__}")


'''
Traceback (most recent call last):
  File "main.py", line 21, in <module>
    class data:
  File "main.py", line 23, in data
    class udata(empobj):
NameError: name 'empobj' is not defined


** Process exited - Return Code: 1 **
Press Enter to exit terminal
'''
        