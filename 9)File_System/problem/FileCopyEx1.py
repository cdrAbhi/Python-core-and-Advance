#Program for Copying the content of one file into another File
#FileCopyEx1.py
srcfile=input("Enter Sourec File:")
try:
	with open(srcfile,"r") as rp:
		dstfile=input("Enter Destination File:")
		with open(dstfile,"a") as wp:
			srcfiledata=rp.read()
			wp.write(srcfiledata)
			print("Src File Content Copied into Dest. File--Verify")
except FileNotFoundError:
	print("Source File Does not Exist")
