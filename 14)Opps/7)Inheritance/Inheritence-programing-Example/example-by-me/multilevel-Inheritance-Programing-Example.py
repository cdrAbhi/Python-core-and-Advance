# lets us assume there exits a university which contains university details like university name its location
# lets us assume there exits a collage which contains collage name and its location accept and display colage details along with university details 
# lets us assume there exist student which contains student number,name and marks accept and display student details along with collage and university deatails
# Do same things using module 
class University:
    def Undetails(self):
        self.uname="University of Everything"
        self.ulocation="Near Shiv Mandir"
    def  disUndetails(self):
        print("==============University Details =====================")
        self.Undetails()
        print(f"University Name: {self.uname}")
        print(f"University Location : {self.ulocation}")

class college(University):
    def colldetails(self):
        self.cnmae="jagdam collage chhapra"
        self.clocation="Near station"
    def discolldetails(self):
        print("==============College Details =====================")
        self.colldetails()
        print("College name : {self.cnmae}")
        print("College location : {self.clocation}")
        

class student(college):
    def Stdetails(self):
        self.num="123"
        self.name="Abhi"
        self.marks=80
    def disStdetails(self):
        self.Stdetails()
        self.disUndetails()
        self.discolldetails()
        print("==============Student Details =====================")        
        print(f"Student number : {self.num}")        
        print(f"Student name : {self.name}")
        print(f"Student Marks : {self.marks}")
        print("*"*50)

sdetail=student()
sdetail.disStdetails()
print(f"Overall data in student class : {sdetail.__dict__}")