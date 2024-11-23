# specifying instance datamember using decorator def __init__(self)

class Student:
    @classmethod
    def getcrs(cls,sln):
        cls.crs="Python"
        cls.sln=sln
        # try:
        #     print(cls.name)
        # except Exception as err:
        #     print(err)
        cls.getcity()
 
    @classmethod
    def getcity(cls):
        cls.city="Hyd"
    
    def __init__(self):
        self.name="Anhi"
        self.mark=60
        self.getdata()
    
    def getdata(self): 
         self.getcrs("First")
         print(f"{self.sln} Student name: {self.name}")
         print(f"{self.sln} Student marks: {self.mark}")        
         print(f"{self.sln} Student course: {self.crs}")
         print(f"{self.sln} Student city: {self.city}")

        
sd=Student()
print(sd.__dict__)

        
        
# prbl-code-1 access instance method from class mthod usnig cls  
# ==============
class Student:
    @classmethod
    def getcrs(cls):  # Class Level Method
        cls.crs = "PYTHON"  # Here crs is called Class Level Data Members
        cls.getcity()  # Calling Class Level Method w.r.t cls

    @classmethod
    def getcity(cls):
        cls.city = "BANG"  # Here city is called Class Level Data Members

    def getdata(self):
        print(self.crs, "=====>", self.city)

# Creating an instance of the Student class
s = Student()

# Calling the class level method to set class level data members
s.getcrs()

# Printing the instance's dictionary to show instance-specific attributes
print(s.__dict__)

# Calling the instance method to display the class level data members
s.getdata()
