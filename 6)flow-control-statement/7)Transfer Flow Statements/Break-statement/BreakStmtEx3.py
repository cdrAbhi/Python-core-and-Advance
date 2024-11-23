#Program for demonstrating break keyword
#BreakStmtEx3.py
s="MISSISSIPPI"
for index,ch in enumerate(s):
    if(index==4):
        break
    print("{}".format(ch),end="")


