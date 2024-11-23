#Program for accepting employee number and get other Details by using un-pickling process.
#EmpUnPickEx3.py
import pickle
def searchemprecord():
	with open("E:\\KVR-PYTHON-9AM\\FILES\\employee.data","rb") as fp:
		eno=int(input("Enter Employee Number for Getting Other Details:"))
		while(True):
			try:
				emprec=pickle.load(fp)
				if(int(emprec[0])==eno):
					print("Emp Name:{}".format(emprec[1]))
					print("Emp Salary:{}".format(emprec[2]))
					print("Emp Desig:{}".format(emprec[3]))
					break
			except EOFError:
				print("Employee Record, {} Emp Number Does not exist".format(eno))
				break

#main program
searchemprecord()