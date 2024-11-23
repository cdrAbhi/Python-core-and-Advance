#DivisionDemo.py--Main Program
from Divsion import divop
from Hyd import HydDivisionError
try:
    a=int(input("Enter Value of a:"))
    b=int(input("Enter Value of b:"))
    res=divop(a,b) # Function call---either gives Result or Exception
except HydDivisionError:
    print("\t\tDon't Enter Zero for Den...")
except:
    print("Some thing went wrong--check!!!")
else:
    print("Div=", res)
finally:
    print("I am from finally Block")
