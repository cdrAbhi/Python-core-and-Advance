#Program for demonstrating  Decorators
#DecEx3.py
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
listwords=getwords(getline) # Decorator Call
listwrd=listwords()
print("List of of Words=",listwrd)
print("----------------------------------------------")
cto=convertupper(listwords)
upperwords=cto()
print("List of uppper words=",upperwords)

