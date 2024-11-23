#program for accepting list of values and Eliminate duplicate Values
#FunctionsEx5.py
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

def getuniquevals(lst):
    if(len(lst)==0):
        print("List is empty--nothing to do")
    else:
        s1=set() #empty list
        for val in lst:
            s1.add(val)
        else:
            print("List of Values:{}".format(lst))
            print("Set of Unique Values={}".format(s1))

#Main program
lst=readvalues()
getuniquevals(lst)