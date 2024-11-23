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
            self.a=int(input("Enter Val1 : "))
            self.b=int(input("Enter Val2 : "))
            print("*"*50)
        
   
v=val()
while True:
    v.getval()
    if v.op=="5":
        print("Thank you for using this program")
        break
    else:
        Arthopr.cal(v)
        
        