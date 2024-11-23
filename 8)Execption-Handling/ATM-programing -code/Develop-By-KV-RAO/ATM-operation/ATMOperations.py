#ATMOperations.py-----File Name and Module Name
from ATMExcept import DepositError,WithDrawError,InSuffFundError
bal=500.00 # here bal is global variable
def  deposit():
	damt=float(input("Enter the Deposit Amount:"))  # Implicitly there is an exception--ValueError
	if(damt<=0):
		raise DepositError
	else:
		global bal
		bal=bal+damt
		print("Ur Account xxxxxx123 Credited with INR:{}".format(damt))
		print("Now Ur Account xxxxxx123 Bal  after Deposit INR:{}".format(bal))

def withdraw():
	global bal
	wamt=float(input("Enter the Withdraw Amount:")) # Implicitly there is an exception--ValueError
	if(wamt<=0):
		raise WithDrawError
	elif((wamt+500)>bal):
		raise InSuffFundError
	else:
		bal=bal-wamt
		print("Ur Account xxxxxx123 Debited with INR:{}".format(wamt))
		print("Now Ur Account xxxxxx123 Bal after withdraw  INR:{}".format(bal))

def  balenq():
	print("Ur Balance in  Account xxxxxx123  INR:{}".format(bal))




