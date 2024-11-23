#Program for demonstrating break keyword
#BreakStmtEx3.py
s="PYTHON"
#My requirement is to display "PYTH" without using slicing and Indexing
i=0
while(i<len(s)):
    if(s[i]=="O"):
        break
    print("\t\t{}".format(s[i]))
    i=i+1
else:
    print("I am from else part of while loop")
print("Other statements in program")