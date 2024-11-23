#Program for Demonstrating Default Arguments
#DefArgsEx3.py
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
dispstudinfo(50,"SR",55.55,"JAVA")
dispstudinfo(60,"DS",15.55)
dispstudinfo(70,"XR",22.22,cnt="USA")
dispstudinfo(80,"SS",33.45,cnt="AUS",crs="HTML")
print("*"*70)