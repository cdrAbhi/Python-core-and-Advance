#Program for Demonstrating continue statement
#ContinueStmtEx3.py
s="PYTHON"
#My Requirment is to disply PYHN
for ch in s:
    if(ch=="T")  or (ch=="O"):
        continue
    print(ch)
else:
    print("i am from else part of for loop")