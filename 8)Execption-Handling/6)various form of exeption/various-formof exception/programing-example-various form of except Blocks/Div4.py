#program for accepting Two Integer Values and find their Div with handling the exceptions
#Div4.py--Not Recommended
try:
	s1=input("Enter First Value:")
	s2=input("Enter Second Value:")
	a=int(s1)    #  Exception generated statement----ValueError
	b=int(s2)  #  Exception generated statement----ValueError
	c=a/b   #  Exception generated statement----ZeroDivisionError
except:
	print("ooooops some thing went wrong!!!!")
else:
	print("--------------------------------------------")
	print("First Value:{}".format(a))
	print("Second Value:{}".format(b))
	print("Div={}".format(c))
	print("--------------------------------------------")
finally:
	print("i am from finally block")