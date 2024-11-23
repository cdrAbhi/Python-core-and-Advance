#Program for Demonstrating Default Arguments
#DefArgsEx1.py
def  dispstudinfo(sno,sname,marks,crs="PYTHON"):
    print("\t{}\t\t{}\t\t{}\t\t{}".format(sno,sname,marks,crs))

#main program
print("*"*50)
print("\tSTNO\tNAME\tMARKS\tCOURSE")
print("*"*50)
dispstudinfo(10,"RS",34.56) # Function Call
dispstudinfo(20,"TR",45.67) # Function Call
dispstudinfo(30,"KV",11.11) # Function Call
dispstudinfo(40,"DR",41.11) # Function Call
print("*"*50)