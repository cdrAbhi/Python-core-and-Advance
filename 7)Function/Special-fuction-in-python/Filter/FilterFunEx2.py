#FilterFunEx2.py
def pos(n):  # Normal Function
    if(n>0):
        return True
    else:
        return False

def neg(n):
    if(n<0):
        return True
    else:
        return False
#main program
print("Enter List of Values Separated Space:")
lst=[int(val) for val in input().split()]
posobj=tuple(filter(pos,lst)) # Filter Concept--here obj is an object of type <class,Filter>
negobj=tuple(filter(neg,lst)) # Filter Concept--here obj is an object of type <class,Filter>
print("Given Elements={}".format(lst))
print("Possitive Elements={}".format(posobj))
print("Negative Elements={}".format(negobj))