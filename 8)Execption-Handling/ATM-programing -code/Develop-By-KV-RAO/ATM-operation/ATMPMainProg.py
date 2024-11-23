#ATMPMainProg.py
from ATMMenu import menu
from ATMExcept import DepositError,WithDrawError,InSuffFundError
from ATMOperations import deposit,withdraw,balenq
import sys
while(True):
	menu()
	try:
		ch=int(input("Enter Ur Choice:"))
		match(ch):
			case 1:
				try:
					deposit()
				except DepositError:
					print("Don't enter -VE OR Zero for Deposit Amount")
				except ValueError:
					print("Don't try to Deposit alnums,strs and symbols for Depositing Amount")
			case 2:
				try:
					withdraw()
				except WithDrawError:
					print("Don't enter -VE OR Zero for Withdrawing Amount:")
				except InSuffFundError:
					print("Ur Account does not have Suff. Funds--Read Python Notes") 
				except ValueError:
					print("Don't try to Withdraw alnums,strs and symbols from Account")
			case 3:
				balenq()
			case 4:
				print("Thx for using this program")
				sys.exit()
			case _:
				print("Ur Selection of Operation Wrong-Try Again")
	except ValueError:
		print("Ur Choice of Operation should not be alnums,strs and symbols")