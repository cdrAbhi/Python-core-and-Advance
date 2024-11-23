#Program for generating even numbers in backward direction from n where n is +ve
#WhileLoopEx3.py
n=int(input("Enter How Many  Even Numbers want to generate  backward Direction:"))
if(n<=1):
    print("{} is invalid input".format(n))
else:
    print("-" * 50)
    print("Even Number from {} to {}".format(n, 2))
    print("-" * 50)
    # is n is odd--decide
    if(n%2!=0):
        n=n-1
    i=n # Init part
    while(i>=2):
        print("\t\t\t{}".format(i))
        i=i-2
    else:
        print("*" * 50)


