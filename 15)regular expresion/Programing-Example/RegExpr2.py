#Program for Searching a word "Python" in given line of text
#RegExpr2.py
import re
gd="Python is an oop lang.python is also fun prog lang"
sp="python"
matres=re.search(sp,gd) # matres--object---<class,re.Match >  OR   <class, "NoneType'>
if(matres!=None):
	print("Search is Sucessful")
	print("Start Index: ",matres.start())
	print("End Index: ",matres.end())
	print("Matched Value: ",matres.group())
else:
	print("Search is Not Sucessful")
