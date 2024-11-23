#FilterFunEx4.py
print("Enter List of Values Separated Space:")
lst=[int(val) for val in input().split()]
posobj=list(filter(lambda n: n>0,lst)) # Filter Concept--here obj is an object of type <class,Filter>
negobj=tuple(filter(lambda k:k<0,lst)) # Filter Concept--here obj is an object of type <class,Filter>
print("Given Elements={}".format(lst))
print("Possitive Elements={}".format(posobj))
print("Negative Elements={}".format(negobj))