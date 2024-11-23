#Program for Demonstrating Keyword Arguments
#KwdArgsEx1.py
def   disp(a,b,c,d):
	print("\t{}\t{}\t{}\t{}".format(a,b,c,d))


#main program
print("="*50)
print("\tA\tB\tC\tD")
print("="*50)
disp(10,20,30,40) # Function call--with Pos args
disp(d=40,a=10,b=20,c=30) # Function call--with Keyword args
disp(10,20,d=40,c=30) # Function call---with Pos args and Keyword args
disp(10,c=30,d=40,b=20)  # Function call---with Pos args and Keyword args
#disp(d=40,20,30,a=10) ----SyntaxError: positional argument follows keyword argument
disp(d=40,b=20,c=30,a=10) # Function call--with Keyword args
print("="*50)