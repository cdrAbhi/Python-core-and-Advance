#GlobalKwdEx2.py
def incr1():
	global a,b #mandatory to use global kwd
	a=a+1
	b=b+1
	
	
def incr2():
	global a,b  #mandatory to use global kwd
	a=a+10
	b=b+10

def  getAB():
	k=a+1 # No need to use global keyword bcoz we are not modifying the globval variable values But we just accessing global Variables
	v=b+1
	r=a+b
	print("in getAB()----Local Variables--->K={},V={},R={}".format(k,v,r))


#main program
a,b=10,20 #global Var
print("In main before incr1()--> a:{}\tb:{}".format(a,b))
incr1() # Function Call
print("In main after incr1()--> a:{}\tb:{}".format(a,b))
incr2()
print("In main after incr2()--> a:{}\tb:{}".format(a,b))
getAB() # Function Call