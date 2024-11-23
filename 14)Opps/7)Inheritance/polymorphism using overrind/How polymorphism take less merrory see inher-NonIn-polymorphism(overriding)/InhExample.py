#Inh Prog
#InhExample.py
class Circle:
	def  draw1(self):
		print("Drawing  Circle")
class Square(Circle):
	def  draw2(self):
		print("Drawing Square")
class Rect(Square):
	def  draw3(self):
		print("Drawing Rect:")

#main program
r=Rect()
r.draw1()
r.draw2()
r.draw3()
