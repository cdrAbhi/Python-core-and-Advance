#program for generating list of prime numbers with in the range of n where n is +ve
#InnerLoopsEx8.py
n=int(input("Enter the Range for listing the primes: "))
if(n<=1):
    print("{} is invalid input".format(n))
else:
    print("List of Primes within{}".format(n))
    for num in range (2,n+1): # outer for loop supply the number
        res=True
        for i in range(2,num):
            if(num%i==0):
                res=False
                break
        if(res):
            print("\t\t{}".format(num))

