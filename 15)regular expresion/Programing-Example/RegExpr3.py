#Program for Searching a word "Python" in given line of text
#RegExpr3.py
import re
gd="Python is an oop lang.Python is also fun prog lang"
sp="Python"
matres=re.finditer(sp,gd)# Here matres is an object of type <class, callable_Iterator>
noc=0
for mat in matres:
	print("Starts Index:{}   End Index:{}  Value:{}".format(mat.start(),mat.end(),mat.group()))
	noc=noc+1
print("Number of Occurences of {}={}".format(sp,noc))