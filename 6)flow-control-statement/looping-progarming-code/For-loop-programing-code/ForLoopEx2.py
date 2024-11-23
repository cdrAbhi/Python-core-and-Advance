#Program for genereating 1 to n numbers by using for loop where n is +ve
#ForLoopEx2.py
n=int(input("Enter How Many Numbers u want to generate:"))
if(n<=0):
    print("{} is invalid Input".format(n))
else:
    print("Numbers within in:{}".format(n))
    print("-"*50)
    for i in range(1,n+1):
        print("\t\t\t{}".format(i))
    else:
        print("*"*50)
