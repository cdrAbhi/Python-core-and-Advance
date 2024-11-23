#Program for generating  n to 1 numbers where n is +VE
#WhileLoopEx2.py
n=int(input("Enter How Many Numbers u want to generate:"))
if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    print("-" * 50)
    print("Number from {} to {}".format(n,1))
    print("-" * 50)
    i=n # Initlization part
    while(i>=1):
        print("\t\t{}".format(i))
        i=i-1
    else:
        print("-"*50)