#Program for Demonstrating Default Arguments
#DefArgsEx4.py
def  dispstudinfo1(sno,sname,marks,crs="PYTHON",cnt="INDIA"):
    print("\t{}\t\t{}\t\t{}\t\t{}\t\t{}".format(sno,sname,marks,crs,cnt))

def  dispstudinfo2(sno,sname,marks,crs="JAVA",cnt="INDIA"):
    print("\t{}\t\t{}\t\t{}\t\t{}\t\t{}".format(sno,sname,marks,crs,cnt))


#main program
print("*"*70)
print("\tSTNO\tNAME\tMARKS\tCOURSE\tCOUNTRY")
print("*"*70)
dispstudinfo1(10,"RS",34.56) # Function Call
dispstudinfo1(20,"TR",45.67) # Function Call
dispstudinfo1(30,"KV",11.11) # Function Call
dispstudinfo1(40,"DR",41.11) # Function Call
dispstudinfo1(90,"DX",41.11,cnt="GER",crs="PHP") # Function Call
print("*"*70)
print("\tSTNO\tNAME\tMARKS\tCOURSE\tCOUNTRY")
print("*"*70)
dispstudinfo2(50,"SR",55.55)
dispstudinfo2(60,"DS",15.55)
dispstudinfo2(70,"XR",22.22,cnt="USA")
dispstudinfo2(80,"SS",33.45)
dispstudinfo2(90,"SQ",33.45,cnt="AUS",crs="HTML")
print("*"*70)