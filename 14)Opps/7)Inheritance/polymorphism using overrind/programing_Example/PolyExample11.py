#PolyExample11.py
class Teacher:
	def  advise(self):
		print("Teacher Advises read 2 Hours Daily")
		print("Teacher advises to Practice 1 Hour Daily")
class SincierStudent(Teacher):
	def advise(self): # Overridden Method
		print("Sincer Student follows Teacher Advises read 2 Hours Daily")
		print("Sincer Student Teacher advises to Practice 1 Hour Daily")
		print("Sincer Student always chat with friends")
		super().advise()

class LazyStudent(Teacher):
	def advise(self): # Overridden Method
		print("LazyStudent never follows Teacher Advises read 2 Hours Daily")
		print("LazyStudent never Teacher advises to Practice 1 Hour Daily")
		print("LazyStudent always chat with friends")
		super().advise()

#Main Program
ss=SincierStudent()
ss.advise()
print("------------------------------------")
ls=LazyStudent()
ls.advise()
