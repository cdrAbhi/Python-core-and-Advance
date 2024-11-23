#Program for Demonstrating continue statement
#ContinueStmtEx4.py
s="PYTHON"
#My Requirment is to disply PYHN
i=0
while(i<len(s)):
    if(s[i]=="T")  or (s[i]=="O"):
        i=i+1
        continue
    print(s[i])
    i=i+1
else:
    print("i am from else part of for loop")