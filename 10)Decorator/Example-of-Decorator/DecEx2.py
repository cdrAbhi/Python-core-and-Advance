#Program for Demonstrating Decorator
#DecEx2.py
def  square(gv):  # Outer Function--Decorator
	def cal(): # Inner Function
		n=gv()
		res=n**2
		return n,res
	return cal

@square
def  getvalue():  # Normal Defined by KVR
	return int(input("Enter Any Numertical value:"))


#main program
n,res=getvalue() # Calling Normal Function
print("Square({})={}".format(n,res))