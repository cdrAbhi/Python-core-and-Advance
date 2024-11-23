#Program for accepting a number and decide wthether it is prime or not
#BreakStmtEx5.py
n=int(input("Enter a Number:"))
if(n<=1):
    print("{} is Invalid Input".format(n))
else:
    res="PRIME"
    for i in range(2,n):
        if(n%i==0):
            res="NOT PRIME"
            break
    if(res=="PRIME"):
        print("{} is {}".format(n,res))
    else:
        print("{} is {}".format(n, res))