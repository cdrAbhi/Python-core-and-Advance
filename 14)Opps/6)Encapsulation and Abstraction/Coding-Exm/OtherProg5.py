#OtherProg5.py
#OtherProg1.py---Data Abstraction
#This Program will not execute bcoz Account Class Made as Hidden ( Class Level Encapuslation)
from Account5 import Account  # Gives ImportError
ac=Account() # Object Creation---
print("Account Number=",ac.acno)
print("Account Holder Name=",ac.cname)
print("Account Holder Bal=",ac.bal)
print("Account Holder Pin=",ac.pin)
print("Account Holder Branch Name=",ac.bname)


