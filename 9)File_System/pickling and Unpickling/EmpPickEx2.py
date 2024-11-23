#Program for accepting employee details and save them in file by using Pickling Process--Program-(A)
#EmpPickEx2.py
import pickle
def saveempdata():
	with open("employee.data","ab") as fp:
		while(True):
			try:
				#accept employee values
				eno=int(input("Enter Employee Number:"))
				ename=input("Enter Employee Name:")
				sal=float(input("Enter Employee Salary:"))
				dsg=input("Enter Employee Designation:")
				# Place the employee in list object
				emplst=list()
				emplst.append(eno)
				emplst.append(ename)
				emplst.append(sal)
				emplst.append(dsg)
				#save the emplst data to file
				pickle.dump(emplst,fp)
				print("Employee Data Saved into File Sucessfully")
				print("*"*50)
				ch=input("Do u want to insert Another Record(yes/no):")
				if(ch.lower()=="no"):
					print("Thx for using this program")
					break
			except ValueError:
				print("Don't enter alnums,strs and symbols for empno and salary:")
			
#main program
saveempdata()
	
