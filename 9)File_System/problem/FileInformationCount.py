#Program for Counting Number of Lines , no. of words and Characters.
#FileInformationCount.py
try:
	srcfile=input("Enter Source File Name:")
	nl,nw,nc=0,0,0
	with open(srcfile,"r") as fp:
		lines=fp.readlines()
		if(len(lines)==0):
			print("File is empty")
		else:
			for line in lines:
				nl=nl+1
				nw=nw+len(line.split())
				nc=nc+len(line)
			else:
				print("Number of Lines={}".format(nl))
				print("Number of Words={}".format(nw))
				print("Number of Characters={}".format(nc))
except FileNotFoundError:
	print("File does not Exist")