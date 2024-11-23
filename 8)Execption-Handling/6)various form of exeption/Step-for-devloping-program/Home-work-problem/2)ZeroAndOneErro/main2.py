#2 write a python progarm which will generate a multiplication table provided the condition must be satisfy
    #  1.Generate an exception when the number is negeative
    #  2.Generate an exception when the number is zero 
    #  3.Generate the multiplication table when the number is positive
# =================================================================================================
 

from NumExe import NegativeErr,ZeroErr 
from mth import mulTbl

try : 
    v=int(input("Enter Numerical Value : "))
    mulTbl(v)
except NegativErr:
    print("Don't Enter Negative Value")
except ZeroErr:
    print("Dont Enter Zero")
finally:
    print("Thank you for using this program")