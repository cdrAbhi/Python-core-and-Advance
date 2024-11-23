#Program for accepting a number and decide wthether it is prime or not
#BreakStmtEx6.py
n=int(input("Enter a Number:"))
if(n<=1):
    print("{} is Invalid Input".format(n))
else:
    res=True
    for i in range(2,n):
        if(n%i==0):
            res=False
            break
    if(res):
        print("{} is  PRIME".format(n))
    else:
        print("{} is NOT PRIME".format(n))

