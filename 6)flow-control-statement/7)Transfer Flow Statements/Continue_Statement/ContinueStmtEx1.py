#Program for Demonstrating continue statement
#ContinueStmtEx1.py
s="PYTHON"
#My Requirment is to disply PYHON
for ch in s:
   if(ch=="T"):
       continue
   print(ch)
else:
    print("i am from else part of for loop")