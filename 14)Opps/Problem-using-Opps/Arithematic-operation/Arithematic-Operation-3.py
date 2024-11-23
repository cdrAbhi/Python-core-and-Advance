"""
After Exception Occur or handling for input in class val fuction call to another( Arthopr) class function-defntion(cal(obj)) and give us another error that op not found.
see below is an error output example:

Output:
========
         Select option to Operation
         ===========================
         1.Sum 
         2.Sub 
         3.Mul 
         4.Div
         5.exit
        ============================
        
Enter option to operation : 1
**************************************************
Enter Val1 : wq1
Invailid Input
ERROR!
Traceback (most recent call last):
  File "<main.py>", line 51, in <module>
  File "<main.py>", line 7, in cal
AttributeError: 'val' object has no attribute 'a'

=== Code Exited With Errors ===

for managing above error we have three method 
                                      1) By Handling exceptin on function calling
                                      1) firs by using sys model which prevent to execute next line of code.
                                      2) By using continue and return True and False
                                      
=========================================================================================================="""

class Arthopr:
    @staticmethod
    def cal(obj):
        match(obj.op):
            case "1":
                print(f"Sum({obj.a},{obj.b}) : {obj.a+obj.b}")
            case "2":
                print(f"Sub({obj.a},{obj.b}) : {obj.a-obj.b}")
            case "3":
                print(f"Mul({obj.a},{obj.b}) : {obj.a*obj.b}")
            case "4":
                try:
                    print(f"Div({obj.a},{obj.b}) : {obj.a//obj.b}")
                except ZeroDivisionError:
                    print("Don't Enter Zero for Denominator")
            case _:
                print("== operation not found ==")
                
class val:
    def getval(self):

        print("""
         Select option to Operation
         ===========================
         1.Sum 
         2.Sub 
         3.Mul 
         4.Div
         5.exit
        ============================
        """)
        
        self.a=int(input("Enter Val1 : "))
        self.b=int(input("Enter Val2 : "))
        print("*"*50)
        self.op=input("Enter option to operation : ")
        print("*"*50)
     
                
   
v=val()
while True:
    try:
        v.getval()
    except ValueError:
        print("Invalid input ")
    else:    
        if v.op=="5":
            print("Thank you for using this program")
            break
        else:
            Arthopr.cal(v)
        
        
==========================================================================================================
import sys
class Arthopr:
    @staticmethod
    def cal(obj):
        match(obj.op):
            case "1":
                print(f"Sum({obj.a},{obj.b}) : {obj.a+obj.b}")
            case "2":
                print(f"Sub({obj.a},{obj.b}) : {obj.a-obj.b}")
            case "3":
                print(f"Mul({obj.a},{obj.b}) : {obj.a*obj.b}")
            case "4":
                try:
                    print(f"Div({obj.a},{obj.b}) : {obj.a//obj.b}")
                except ZeroDivisionError:
                    print("Don't Enter Zero for Denominator")
            case _:
                print("== operation not found ==")
                
class val:
    def getval(self):

        print("""
         Select option to Operation
         ===========================
         1.Sum 
         2.Sub 
         3.Mul 
         4.Div
         5.exit
        ============================
        """)
        self.op=input("Enter option to operation : ")
        print("*"*50)
        if self.op in ["1","2","3","4"]:
            try:        
                self.a=int(input("Enter Val1 : "))
                self.b=int(input("Enter Val2 : "))
                print("*"*50)
            except ValueError:
                print("Invailid Input")
                sys.exit()
   
v=val()
while True:
    v.getval()
    if v.op=="5":
        print("Thank you for using this program")
        break
    else:
        Arthopr.cal(v)
        
        




#=============================OR==========================================


class Arthopr:
    @staticmethod
    def cal(obj):
        match obj.op:
            case "1":
                print(f"Sum({obj.a},{obj.b}) : {obj.a+obj.b}")
            case "2":
                print(f"Sub({obj.a},{obj.b}) : {obj.a-obj.b}")
            case "3":
                print(f"Mul({obj.a},{obj.b}) : {obj.a*obj.b}")
            case "4":
                try:
                    print(f"Div({obj.a},{obj.b}) : {obj.a//obj.b}")
                except ZeroDivisionError:
                    print("Don't Enter Zero for Denominator")
            case _:
                print("== operation not found ==")
                
class val:
    def getval(self):

        print("""
         Select option to Operation
         ===========================
         1.Sum 
         2.Sub 
         3.Mul 
         4.Div
         5.exit
        ============================
        """)
        self.op=input("Enter option to operation : ")
        print("*"*50)
        if self.op in ["1","2","3","4"]:
            try:        
                self.a=int(input("Enter Val1 : "))
                self.b=int(input("Enter Val2 : "))
                print("*"*50)
            except ValueError:
                print("Invalid Input")
                return False
        return True        
                
   
v=val()
while True:
    if not v.getval()
      continue
    if v.op=="5":
        print("Thank you for using this program")
        break
    else:
        Arthopr.cal(v)
        
    