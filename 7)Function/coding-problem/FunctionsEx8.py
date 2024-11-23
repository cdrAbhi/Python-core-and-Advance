#program for accepting list of values and find max and min elements without using max() and min pre-defined functions
#FunctionsEx7.py
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
def  findmax(lst):  # lst= 10,20,5,30,25,45,12]
    maxv=lst[0]
    for val in lst:
        if(maxv<val):
            maxv=val
    else:
        return maxv

def findmin(lst):
    minv=lst[0]
    for val in lst:
        if(minv>val):
            minv=val
    else:
        return minv
#main program
lst=readvalues()
if(len(lst)==0):
    print("List is empty--can't find max and min")
elif(len(lst)==1):
    print("Max and Min is Same={}".format(lst[0]))
elif(len(set(lst))==1):
    print("All Values are Equal and Max and Min is Same={}".format(lst[0]))
else:
    maxv=findmax(lst)
    minv=findmin(lst)
    print("Max({})={}".format(lst,maxv))
    print("Min({})={}".format(lst,minv))
