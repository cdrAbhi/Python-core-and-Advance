#Program for Demonstrating Keyword Arguments
#KwdArgsEx2.py
def  dispstudinfo(sno,sname,marks,crs="PYTHON",cnt="INDIA"):
    print("\t{}\t{}\t{}\t{}\t{}".format(sno,sname,marks,crs,cnt))

#main program
print("*"*70)
print("\tSTNO\tNAME\tMARKS\tCOURSE\tCOUNTRY")
print("*"*70)
dispstudinfo(10,"RS",34.56) # Function Call
dispstudinfo(sname="DR",sno=20,marks=33.33)
dispstudinfo(30,crs="Java",cnt="USA",sname="TR",marks=33.78)
print("*"*70)