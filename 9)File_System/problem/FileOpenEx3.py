#Program for Demonstrating How to Open the file in different Modes
#FileOpenEx3.py
with open("kvr1.py","w") as fp:  # here fp is an object TextIOWrapper
	print("---------------------------------------------------------------")
	print("File Openned in write Mode Successfully")
	print("Type of fp=",type(fp))
	print("---------------------------------------------------------------")
	print("Proeprties of File")
	print("---------------------------------------------------------------")
	print("\tFile Name:=",fp.name)
	print("\tFile Mode=",fp.mode)
	print("\tIs File Readable=",fp.readable())
	print("\tIs file writable=",fp.writable())
	print("\tIs File Closed=",fp.closed)
	print("---------------------------------------------------------------")
print("************************************************************")
print("\tIs File Closed after with open() as =",fp.closed)


