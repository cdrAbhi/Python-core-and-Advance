#Program for Demonstrating Possitional Arguments
#PossArgsEx1.py

def  dispstudinfo(sno,sname,marks):
    print("\t{}\t\t{}\t\t{}".format(sno,sname,marks))

#main program
print("*"*50)
print("\tSTNO\tNAME\tMARKS")
print("*"*50)
dispstudinfo(10,"RS",34.56) # Function Call
dispstudinfo(20,"TR",45.67)
dispstudinfo(30,"KV",11.11)
print("*"*50)