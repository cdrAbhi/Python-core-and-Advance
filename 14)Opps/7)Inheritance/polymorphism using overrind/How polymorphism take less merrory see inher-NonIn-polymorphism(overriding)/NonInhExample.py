#Non-Inh Prog
#NonInhExample.py
class Circle:
	def  draw1(self):
		print("Drawing  Circle")
class Square:
	def  draw2(self):
		print("Drawing Square")
class Rect:
	def  draw3(self):
		print("Drawing Rect:")

#main program
c=Circle()
s=Square()
r=Rect()
c.draw1()
s.draw2()
r.draw3()
