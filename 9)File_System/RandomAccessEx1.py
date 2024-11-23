#Program for Demonstrating Random Access Files
#RandomAccessEx1.py
with open("E:\\KVR-PYTHON-9AM\\FILES\\NOTES\\sample.data","r") as fp:
	print("-"*50)
	print("Intial Position of fp=",fp.tell())
	filedata=fp.read(6)
	print(filedata)
	print("-"*50)
	print("Now Position of fp=",fp.tell())
	filedata=fp.read(4)
	print(filedata)
	print("-"*50)
	print("Now Position of fp=",fp.tell())
	filedata=fp.read(2)
	print(filedata)
	print("-"*50)
	print("Now Position of fp=",fp.tell())
	print("-"*50)
	filedata=fp.read(2)
	print("New Line=",filedata)
	print("-"*50)
	print("Now Position of fp=",fp.tell())
	print("-"*50)
	filedata=fp.read(3)
	print("New Line=",filedata)
	print("-"*50)
	filedata=fp.read()
	print(filedata)
	print("-"*50)
	print("Now Position of fp=",fp.tell()) # Here fp pointing to last part of file
	print("-"*50)
	#Reset the file pointer to Desired index 
	fp.seek(6)
	print("Now Position of fp after seek=",fp.tell())
	print("*************************************************")
	filedata=fp.read()
	print(filedata)
	print("Now Position of fp =",fp.tell())
	print("*************************************************")
	filedata=fp.read()
	print("After Reaching End of file, File Data=",filedata)
	print("*************************************************")







	