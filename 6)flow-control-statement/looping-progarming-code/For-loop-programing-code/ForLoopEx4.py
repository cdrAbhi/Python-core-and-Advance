#Program for genereating  even numbers numbers by using for loop where n is +ve
#ForLoopEx4.py
n=int(input("Enter How Many Numbers u want to generate:"))
if(n<=0):
    print("{} is invalid Input".format(n))
else:
    print("Even Numbers within in:{}".format(n))
    for i in range(2,n+1,2):
        print("\t\t\t{}".format(i))
