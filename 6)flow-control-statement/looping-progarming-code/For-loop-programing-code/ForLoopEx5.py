#Program for genereating  Odd numbers numbers by using for loop where n is +ve
#ForLoopEx5.py
n=int(input("Enter How Many Numbers u want to generate:"))
if(n<=0):
    print("{} is invalid Input".format(n))
else:
    print("Odd Numbers within in:{}".format(n))
    for i in range(1,n+1,2):
        print("\t\t\t{}".format(i))
