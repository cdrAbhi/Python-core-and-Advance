#FunctionsEx1.py
def dispvalues1(lst):
    print("---------------------------------------")
    print("Type of lst=",type(lst))
    for val in lst:
        print(val)
    print("-------------------------------------------")

def  dispvalues2(dobj):
    print("---------------------------------------")
    print("Type of dobj=", type(dobj))
    for k,v in dobj.items():
        print("\t{}--->{}".format(k,v))
    print("---------------------------------------")

#main program
lst1=[10,"Rossum",34.56,True,2+3j]
dispvalues1(lst1) # Function call with list
tpl=(100,200,100,400,600)
dispvalues1(tpl) # Function call with tuple object
st1={10,12.34,5.6,True,2+3j}
dispvalues1(st1) # Function call with set object
d1={10:"Python",20:"Java",30:"HTML",40:"C"}
dispvalues2(d1) # Function call with dict object
