#reduceEx4.py
import functools
print("Enter List of Words separated by comma:")
lst=[str(val) for val in input().split(",")] # [ Python, is, an , oop, lang]
print("Given List of Words={}".format(lst))
line=functools.reduce(lambda word1,word2 : word1+" "+word2 , lst)
print("Line: {}".format(line))