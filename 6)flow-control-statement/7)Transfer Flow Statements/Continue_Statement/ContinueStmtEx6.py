#Program accepting list of values and get +Ve and -Be list of Values
#ContinueStmtEx6.py
nov=int(input("Enter How Many Values u have:"))
if(nov<=0):
    print("{} invalid Input".format(nov))
else:
    lst=list()
    for i in range(1,nov+1):
        val=float(input("Enter {} Value:".format(i)))
        lst.append(val)
    else:
        print("-"*50)
        print("List of Values:{}".format(lst))#[10.0, -20.0, 30.0, -40.0, 0.0]
        print("-"*50)
        #Code for obtaining list of +Ve Values
        pslist=[] # create empty list for appending +ve values
        for val in lst:
            if(val<=0):
                continue
            pslist.append(val)
        else:
            # Code for obtaining list of -Ve Values
            nslist=list() # create empty list for appending -ve values
            for val in lst:
                if(val>=0):
                    continue
                nslist.append(val)
            else:
                print("List of +VE Values:{}".format(pslist))
                print("List of -VE Values:{}".format(nslist))
                print("-" * 50)
