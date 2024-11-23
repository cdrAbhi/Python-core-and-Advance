#Program for Demonstrating variable length args
#This Program will  execute as it is
#VarLenArgsEx2.py
def disp(a,b,c,d,e): # Function Def-1
    print(a,b,c,d,e)
disp(10,20,30,40,50) # Function Call-1 with 5 args
#-------------------------------------------------------------
def disp(a,b,c,d): # Function Def-2
    print(a,b,c,d)
disp(10,20,30,40) # Function Call-2 with 4 args
#--------------------------------------------------------------
def disp(a,b,c): # Function Def-3
    print(a,b,c)
disp(10,20,30) # Function Call-3 with 3 args
#--------------------------------------------------------------
def disp(a,b): # Function Def-4
    print(a,b)
disp(10,20) # Function Call-4 with 2 args
#--------------------------------------------------------------
def disp(a): # Function Def-5
    print(a)
disp(10) # Function Call-5 with 1 args
#--------------------------------------------------------------
def disp(): # Function Def-6
    print("empty")
#--------------------------------------------------------------
disp() # Function Call-6 with Zero args