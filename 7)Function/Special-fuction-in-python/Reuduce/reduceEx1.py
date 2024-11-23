#reduceEx1.py
import functools
print("Enter  Values for  List:")
lst1=[int(val) for val in input().split()]
res=functools.reduce(lambda x,y: x+y, lst1)
print("sum({})={}".format(lst1,res))
