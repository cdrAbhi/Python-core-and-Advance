#Program for cal sum of two nums by using functions
"""INPUT        :   Taken from Function call
PROCESS :   Done in Function Body
RESULT     :  Displayed in Function Call """
#ApproachEx1.py
def addop(k,v):  # Function Definition
    r=k+v # Here 'r' is called Local Variable
    return r

#main program
a=float(input("Enter Value of a:"))
b=float(input("Enter Value of b:"))
res=addop(a,b) # Function Call
print("sum({},{})={}".format(a,b,res))
print("---------------------------------------------------")
k=float(input("Enter Value of k:"))
v=float(input("Enter Value of v:"))
r=addop(k,v)
print("{}+{}={}".format(k,v,r))

