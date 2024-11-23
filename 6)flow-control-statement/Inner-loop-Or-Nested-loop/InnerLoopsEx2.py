#while Loop in while loop
#InnerLoopsEx2.py
i=1
while(i<=5): # Outer loop
    print("Outer Loop--i={}".format(i))
    print("--------------------------------------")
    j=1
    while(j<=3): # Inner Loop
        print("\t\tInner Loop --j:{}".format(j))
        j=j+1
    else:
        i=i+1
        print("--------------------------------------")
else:
    print("--------------------------------------")
