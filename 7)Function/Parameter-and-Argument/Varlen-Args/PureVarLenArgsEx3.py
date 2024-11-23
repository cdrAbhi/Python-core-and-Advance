#Program for Demonstrating variable length args
#PureVarLenArgsEx3.py
def  disp( *a):# here *a is called Variable length param and whose type is tuple
    s=0
    for val in a:
        print("{}".format(val),end=" ")
        s=s+val
    else:
        print("sum={}".format(s))
        print("-------------------------------")

#main program
disp(10,20,30,40,50) # Function Call-1 with 5 args
disp(10,20,30,40) # Function Call-2 with 4 args
disp(10,20,30) # Function Call-3 with 3 args
disp(10,20) # Function Call-4 with 2 args
disp(10) # Function Call-5 with 1 args
disp() # Function Call-6 with Zero args