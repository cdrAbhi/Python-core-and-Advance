#FilterFunEx1.py
def pos(n):  # Normal Function
    if(n>0):
        return True
    else:
        return False

#main program
lst=[10,-20,-30,40,-50,0,60,-70]
obj=filter(pos,lst) # Filter Concept--here obj is an object of type <class,Filter>
#Type cast filter class object into list / tuple / set
pslist=list(obj)
print("Given Elements={}".format(lst))
print("Possitive Elements={}".format(pslist))