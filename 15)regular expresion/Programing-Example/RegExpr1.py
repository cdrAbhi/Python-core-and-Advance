#Program for Searching a word "Python" in given line of text
#RegExpr1.py
import re
gd="Python is an oop lang.Python is also fun prog lang"
sp="Python"
res=re.findall(sp,gd) # Here res is of type list
print("Number of occurences of {}={}".format(sp,len(res)))

