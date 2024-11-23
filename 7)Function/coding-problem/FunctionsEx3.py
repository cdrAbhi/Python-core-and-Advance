#Program accepting list of values and find sum and avg without using sum()
#FunctionsEx3.py
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
            print("sum({})={}".format(lst,s))
            avg=findavg(s,len(lst)) # Function Call
            print("Avg({})={}".format(lst,avg))
def findavg(s,nov):
    av=s/nov
    return av

#Main program
lst=readvalues() # Function Call
findsum(lst) # Function call

