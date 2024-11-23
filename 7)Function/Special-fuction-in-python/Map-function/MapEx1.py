#MapEx1.py
def square(value):
    return (value**2)

def squareroot(value):
    return (value**0.5)
#main program
print("Enter List of Numerical Values")
lst=[float(val) for val in input().split()]
obj=map(square,lst) # Map Concept--here obj is an object of class of Map
obj1=map(squareroot,lst) # Map Concept--here obj is an object of class of Map
#Convert Map Object into list type
sqlist=list(obj)
sqrtlist=list(obj1)
print("="*50)
print("Given Number\t\tSquare\t\t\t\tSquareRoot")
print("="*50)
for n,sqr,sqrtv in zip(lst,sqlist,sqrtlist):
    print("\t{}\t\t\t\tsqr({})={}\t\tsqrt({})={}".format(n,n,round(sqr,2),n,round(sqrtv,2)))
print("="*50)