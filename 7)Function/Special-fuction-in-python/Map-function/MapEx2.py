#MapEx2.py
print("Enter List of Numerical Values")
lst=[float(val) for val in input().split()]
sqlist=list(map(lambda value: value**2,lst) )
sqrtlist=list(map(lambda value:value**0.5,lst) )# Map Concept--here obj is an object of class of Map
print("="*50)
print("Given Number\t\tSquare\t\t\t\tSquareRoot")
print("="*50)
for n,sqr,sqrtv in zip(lst,sqlist,sqrtlist):
    print("\t{}\t\t\t\tsqr({})={}\t\tsqrt({})={}".format(n,n,round(sqr,2),n,round(sqrtv,2)))
print("="*50)