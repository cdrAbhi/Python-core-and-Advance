#Program accepting list of values and find sum and avg without using sum()
#FunctionsEx2.py
def  readvalues():
    lst=[]
    print("Enter List of Values and press @ to stop:")
    while(True):
        value=input()
        if(value!="@"):
            lst.append(float(value))
        else:
            break
    return lst

def  findsum(lst):
    if(len(lst)==0):
       print("List is empty-can't find sum")
    else:
        s=0
        for val in lst:
            s=s+val
        else:
            print("sum={}".format(s))
            print("Avg={}".format(s/len(lst)))

#Main program
lst=readvalues() # Function Call
findsum(lst) # Function call

