#Program for generating 1 to n numbers where n is +VE
#WhileLoopEx1.py
n=int(input("Enter How Many Numbers u want to generate:"))# n=10
if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    #logic for generating 1 to n numbers
    i=1 # Initlization Part
    while(i<=n):  # Test Cond
        print("{}".format(i))
        i=i+1 # Updation Part
    else:
        print("I am from else-part of while loop")
print("Program execution Completed")

