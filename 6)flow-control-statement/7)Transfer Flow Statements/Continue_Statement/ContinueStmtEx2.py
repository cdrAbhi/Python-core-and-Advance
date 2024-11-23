#Program for Demonstrating continue statement
#ContinueStmtEx2.py
s="PYTHON"
#My Requirment is to disply PYHON
i=0
while(i<len(s)):
    if(s[i]=="T"):
        i=i+1
        continue
    print(s[i])
    i=i+1
else:
    print("i am from else part of while loop")