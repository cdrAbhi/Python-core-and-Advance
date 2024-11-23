#Program for cal sum of two nums by using functions
"""INPUT        :   Taken in  Function Body
PROCESS :       Done in Function Body
RESULT     :   Displayed in Function Call """
#ApproachEx4.py
def  sumop():
    #Input
    k=float(input("Enter Value of k:"))
    v = float(input("Enter Value of v:"))
    #Process
    r=k+v
    #give result to Function call
    return k,v,r # return statement not only returns one value but also more number values
#main program
a,b,c=sumop() # Function Call with Multi Line assignment
print("sum({},{})={}".format(a,b,c))
print("------------------------------------------------")
res=sumop() # Function Call with single line assignment
#here res is type <class,tuple>
print("sum({},{})={}".format(res[0],res[1],res[2]))
print("-------------------OR-----------------------------")
print("sum({},{})={}".format(res[-3],res[-2],res[-1]))
print("-------------------OR-----------------------------")
print("sum({},{})={}".format(res[0:1],res[1:2],res[2:]))