#Program without Decorator
#Non-DecEx1.py
def  getvalue():
	return float(input("Enter any Numericval Number:"))

def square():
	n=getvalue()
	res=n**2
	print("Square({})={}".format(n,res))

#main programn
square()