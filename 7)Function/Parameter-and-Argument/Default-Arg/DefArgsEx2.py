#Program for Demonstrating Default Arguments
#DefArgsEx2.py
def  dispstudinfo(sno,sname,marks,crs="PYTHON",cnt="INDIA"):
    print("\t{}\t\t{}\t\t{}\t\t{}\t\t{}".format(sno,sname,marks,crs,cnt))

#main program
print("*"*70)
print("\tSTNO\tNAME\tMARKS\tCOURSE\tCOUNTRY")
print("*"*70)
dispstudinfo(10,"RS",34.56) # Function Call
dispstudinfo(20,"TR",45.67) # Function Call
dispstudinfo(30,"KV",11.11) # Function Call
dispstudinfo(40,"DR",41.11) # Function Call
print("*"*70)