#FilterFunEx3.py
pos=lambda n : n>0 # Anonymous Function
neg=lambda k: k<0 # Anonymous Function
#main program
print("Enter List of Values Separated Space:")
lst=[int(val) for val in input().split()]
posobj=list(filter(pos,lst)) # Filter Concept--here obj is an object of type <class,Filter>
negobj=tuple(filter(neg,lst)) # Filter Concept--here obj is an object of type <class,Filter>
print("Given Elements={}".format(lst))
print("Possitive Elements={}".format(posobj))
print("Negative Elements={}".format(negobj))