#Program for finding Biggest of Two Numbers and Check for Equality
#IfElseStmtEx2.py
a=float(input("Enter Value of a:"))#a=100
b=float(input("Enter Value of b:"))#b=200
if(a>b):
    print("Big(a=:{},b:{})={}".format(a,b,a))
else:
    if(b>a):
        print("Big(a=:{},b:{})={}".format(a, b, b))
    else:
        print("Both Values are equal")


