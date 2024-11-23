#Program for Demonstrating Possitional Arguments
#PossArgsEx1.py
def  dispstudinfo(sno,sname,marks,crs):
    print("\t{}\t\t{}\t\t{}\t\t{}".format(sno,sname,marks,crs))

#main program
print("*"*50)
print("\tSTNO\tNAME\tMARKS\tCOURSE")
print("*"*50)
dispstudinfo(10,"RS",34.56,"PYTHON") # Function Call
dispstudinfo(20,"TR",45.67,"PYTHON") # Function Call
dispstudinfo(30,"KV",11.11,"PYTHON") # Function Call
dispstudinfo(40,"DR",41.11,"PYTHON") # Function Call
print("*"*50)