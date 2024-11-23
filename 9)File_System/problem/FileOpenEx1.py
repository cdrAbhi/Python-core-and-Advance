#Program for Demonstrating How to Open the file in different Modes
#FileOpenEx1.py
try:
	fp=open("kvr.data","r")
	print("File Opened in Read Mode Sucessfully")
	print("Type of fp=",type(fp))
except FileNotFoundError:
	print("File Does not Exist")
