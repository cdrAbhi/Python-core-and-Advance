#FilterMapEx1.py
print("Enter Values for  List:")
lst=[int(val) for val in input().split()]
print("Given List of Values:{}".format(lst)) # [10, 20, -4, -6, 12, 6, -6]
poslst=list(filter(lambda value: value>0,lst))
neglst=list(filter(lambda value: value<0,lst))
sqrposlst=list(map(lambda value: value**2,poslst))
qblst=list(map(lambda value: value**3,neglst))
print("Square List:{}".format(sqrposlst))
print("Cube List:{}".format(qblst))



