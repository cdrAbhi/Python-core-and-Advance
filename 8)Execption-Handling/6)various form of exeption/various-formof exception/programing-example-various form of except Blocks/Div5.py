#program for accepting Two Integer Values and find their Div with handling the exceptions
#Div5.py---Developed by KVR in 2023 Dec 21 at 10:38AM 
#KVR-----This will come maintainance in 2025---need to add come code--V.Gopal
try:
	s1=input("Enter First Value:")
	s2=input("Enter Second Value:")
	a=int(s1)    #  Exception generated statement----ValueError
	b=int(s2)  #  Exception generated statement----ValueError
	c=a/b   #  Exception generated statement----ZeroDivisionError
	s="PYTHON" # 2025
	print(s[10])
except ZeroDivisionError:
	print("\tDon't Enter Zero for Den..")
except ValueError:
	print("\tDon't Enter alnums,strs and special symbols")
except IndexError:
	print("\tPlz check Index")
except:  # Default except block
	print("ooops some thing went wrong!!!")
else:
	print("--------------------------------------------")
	print("First Value:{}".format(a))
	print("Second Value:{}".format(b))
	print("Div={}".format(c))
	print("--------------------------------------------")
finally:
	print("i am from finally block")