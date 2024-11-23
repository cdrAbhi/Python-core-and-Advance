#Program for demonstrating  Decorators
#DecEx5.py
def convertupper(lw):
	def converttoupper():
		line,words=lw()
		lst=[]
		for word in words:
			lst.append(word.upper())
		return line,words,lst
	return converttoupper

def  getwords(GL):
	def  words():
		line=GL()
		ws=line.split()
		return line,ws
	return words

@convertupper
@getwords
def  getline():
	return input("Enter a Line of Text:")



#main program
lstwords=getline() # here lstwords is an object of tuple
print("=============================")
print("Given Line={}".format(lstwords[0]))
print("Given Words={}".format(lstwords[1]))
print("Given Words in Caps=",lstwords[2])
print("=============================")