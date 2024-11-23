#reduceEx3.py
import functools
print("Enter  Values for  List:")
lst1=[int(val) for val in input().split()]
bigv=functools.reduce(lambda a,b: a if a>b else b, lst1)
smv=functools.reduce(lambda a,b: a if a<b else b, lst1)
print("Big({})={}".format(lst1,bigv))
print("Small({})={}".format(lst1,smv))