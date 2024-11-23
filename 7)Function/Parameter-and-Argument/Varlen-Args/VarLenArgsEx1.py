#Program for Demonstrating variable length args
#This Program will not execute as it is bcoz PVM remembers the latest function definition due Its Interpretation Process
#VarLenArgsEx1.py
def disp(a,b,c,d,e): # Function Def-1
    print(a,b,c,d,e)
def disp(a,b,c,d): # Function Def-2
    print(a,b,c,d)
def disp(a,b,c): # Function Def-3
    print(a,b,c)
def disp(a,b): # Function Def-4
    print(a,b)
def disp(a): # Function Def-5
    print(a)
def disp(): # Function Def-6
    print("empty")

#main program
disp(10,20,30,40,50) # Function Call-1 with 5 args
disp(10,20,30,40) # Function Call-2 with 4 args
disp(10,20,30) # Function Call-3 with 3 args
disp(10,20) # Function Call-4 with 2 args
disp(10) # Function Call-5 with 1 args
disp() # Function Call-6 with Zero args