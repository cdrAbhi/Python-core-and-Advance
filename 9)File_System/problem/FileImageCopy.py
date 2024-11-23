#program for copiyng an image 
#FileImageCopy.py
try:
	with open("E:\\KVR-PYTHON-9AM\\FILES\\NOTES\\kvr.png","rb") as rp:
		with open("pt.png","ab") as wp:
			srcfiledata=rp.read()
			wp.write(srcfiledata)
			print("Src File Image  Copied into Dest. File--Verify")
except FileNotFoundError:
	print("Source File Does not Exist")
