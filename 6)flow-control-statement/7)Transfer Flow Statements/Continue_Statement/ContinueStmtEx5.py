#Program for Demonstrating continue statement
#ContinueStmtEx4.py
s="PYTHON"
#My Requirment is to disply PYHN
i=0
while(i<len(s)):
    if s[i] in ["T","O","Y"]:
        i=i+1
        continue
    print(s[i])
    i=i+1
else:
    print("i am from else part of for loop")