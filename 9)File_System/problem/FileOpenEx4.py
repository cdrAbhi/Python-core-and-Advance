#Program for Demonstrating How to Open the file in different Modes
#FileOpenEx4.py
try:
	fp=open("kvr1.py","r")  # here fp is an object TextIOWrapper
except FileNotFoundError:
	print("File Does not Exist")
else:
	print("---------------------------------------------------------------")
	print("File Openned in Read Mode Successfully")
	print("Type of fp=",type(fp))
	print("---------------------------------------------------------------")
	print("Proeprties of File")
	print("---------------------------------------------------------------")
	print("\tFile Name:=",fp.name)
	print("\tFile Mode=",fp.mode)
	print("\tIs File Readable=",fp.readable())
	print("\tIs file writable=",fp.writable())
	print("\tIs File Closed in else block=",fp.closed)
	print("---------------------------------------------------------------")
finally:
	fp.close() # Manual Closing 
	print("\tIs File Closed in finally Block =",fp.closed)


