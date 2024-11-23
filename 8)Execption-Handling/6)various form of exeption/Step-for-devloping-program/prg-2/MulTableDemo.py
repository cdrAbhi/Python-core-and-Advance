#MulTableDemo.py--Main program
from MulTable import multable
from MulExcept import ZeroError,NegNumError
try:
    multable(int(input("Enter a number for generating mul table:")))
except ZeroError:
    print("Don't enter zero for Mul Table")
except NegNumError:
    print("Don't enter -VE Number for Mul Table")
except ValueError:
    print("Don't enter alnums,strs and symbols for Mul table")
except :
    print("Some went wrong--check")
