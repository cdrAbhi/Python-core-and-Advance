#Program for Demonstrating Inheritance
#InhProg4.py
class GrandParent:
	def  getGrandParentProp(self):
		self.gp=float(input("Enter Grand Parent Property:"))

class Parent:
	def  getParentProp(self):
		self.pp=float(input("Enter Parent Property:"))

class Child(GrandParent,Parent):
	def  getChildProp(self):
		self.cp=float(input("Enter Child Property:"))
	def computetotprop(self):
		self.totprop=self.gp+self.pp+self.cp
	def  dispprop(self):
		self.getGrandParentProp()
		self.getParentProp()
		self.getChildProp()
		self.computetotprop()
		print("*"*40)
		print("\tProperty Details")
		print("*"*40)
		print("\tGrand Parent Property:{}".format(self.gp))
		print("\tParent Property:{}".format(self.pp))
		print("\tChild Property:{}".format(self.cp))
		print("\tTotal Property:{}".format(self.totprop))
		print("*"*40)

#Main Prog
c=Child()
c.dispprop()