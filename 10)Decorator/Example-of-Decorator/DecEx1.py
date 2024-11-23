#Program for Demonstrating Decorator
#DecEx1.py
def  getvalue():  # Normal Defined by KVR
	return int(input("Enter Any Numertical value:"))

def  square( gv  ):  # Outer Function Name
	def  compute(): # Inner Function Name
		n=gv()
		res=n**2
		return n,res
	return compute

#main program
comp=square(getvalue)  # Function Call--Taking another Function name as Parameter--Decorator Call
print("type of comp=",type(comp))
n,result=comp()
print("Square({})={}".format(n,result))
