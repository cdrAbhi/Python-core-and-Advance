#Program for Demonstrating variable length args
#PureVarLenArgsEx6.py
def  disp(sno,sname, *a,city="HYD"):# here *a is called Variable length param and whose type is tuple
	print("Student Number:{}".format(sno))
	print("Student Name:{}".format(sname))
	print("Student City:{}".format(city))
	s=0
	for val in a:
		print("{}".format(val),end=" ")
		s=s+val
	else:
		print("sum={}".format(s))
		print("-------------------------------")

#main program
disp(100,"RS",10,20,30,40,50,city="USA") # Function Call-1 with 5 args
disp(200,"TR",10,20,30,40) # Function Call-2 with 4 args
#disp(300,"SR",city="AUS",10,20,30) # Function Call-3 with 3 args--SyntaxError: positional argument follows keyword argument
disp(400,"DR",10,20) # Function Call-4 with 2 args
disp(500,"XR",10,city="AUS") # Function Call-5 with 1 args
disp(600,"KV") # Function Call-6 with Zero args
disp(100,10,20,30,40,50,sname="tr")