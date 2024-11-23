#Program for Demonstrating Inheritance
#InhProg2.py
class Parent:
	def  getParentProp(self):
		self.pp=float(input("Enter Parent Property:"))

class Child(Parent):
	def  getChildProp(self):
		self.cp=float(input("Enter Child Property:"))
	def computetotprop(self):
		self.totprop=self.pp+self.cp
	def  dispprop(self):
		print("*"*40)
		print("\t\tProperty Details")
		print("*"*40)
		print("\t\tParent Property:{}".format(self.pp))
		print("\t\tChild Property:{}".format(self.cp))
		print("\t\tTotal Property:{}".format(self.totprop))
		print("*"*40)

#Main Prog
c=Child()
c.getParentProp()
c.getChildProp()
c. computetotprop()
c.dispprop()