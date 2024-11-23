#Program for demonstrating  Decorators
#DecEx4.py
def  getline():
	return input("Enter a Line of Text:")

def  getwords(GL):
	def  words():
		line=GL()
		ws=line.split()
		return ws
	return words

def convertupper(lw):
	def converttoupper():
		words=lw()
		lst=[]
		for word in words:
			lst.append(word.upper())
		return lst
	return converttoupper

#main program
lstwords=convertupper(getwords(getline)) ()
print("List of Cap Words=",lstwords)

