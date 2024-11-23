#program for Generating 1 to n mul tables where n is +ve
#nnerLoopsEx6.py
n=int(input("Enter How Many Mul Tables u want:"))
if(n<=0):
    print("{} is invalid input".format(n))
else:
    for i in range(1,n+1): # Outer loop supply a number
        print("="*50)
        print("Mul Table for: {}".format(i))
        print("=" * 50)
        for j in range(1,11): # Inner Loop--generates mul table
            print("\t\t{} x {}={}".format(i,j,i*j))
        else:
            print("=" * 50)
