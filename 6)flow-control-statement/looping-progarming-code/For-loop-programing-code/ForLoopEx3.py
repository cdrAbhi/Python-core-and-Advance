#Program for genereating  n to 1 numbers by using for loop where n is +ve
#ForLoopEx3.py
n=int(input("Enter How Many Numbers u want to generate:"))
if(n<=0):
    print("{} is invalid Input".format(n))
else:
    print("Numbers within in:{}".format(n))
    for i in range(n,0,-1):
        print("\t\t\t{}".format(i))
