#program for accepting list of values and Eliminate duplicate Values
#FunctionsEx6.py
def  readvalues():
    lst=[]
    print("Enter List of Values and press @ to stop:")
    while(True):
        value=input()
        if(value!="@"):
            lst.append(value)
        else:
            break
    return lst
def  getuniqueelements():
    lst=readvalues()
    if(len(lst)==0):
        print("List is empty--nothing to do any operation:")
    else:  # lst=[10,20,10,30,20,10,40,50]
        ulist=[] #empty list--10
        for val in lst:
            if val not in ulist:
                ulist.append(val)
        else:
            print("Given List:{}".format(lst))
            print("Unique Elements={}".format(ulist))

#main program
getuniqueelements()


