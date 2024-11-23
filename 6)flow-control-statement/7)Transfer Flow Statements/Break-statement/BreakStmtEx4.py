#BreakStmtEx4.py
s="MISSISSIPPI"
cnt=s.count("I")
icnt=1
for ch in s:
    if(ch=="I") and (icnt==2):
        break
    else:
        print(ch)
        if(ch=="I"):
            icnt=icnt+1
