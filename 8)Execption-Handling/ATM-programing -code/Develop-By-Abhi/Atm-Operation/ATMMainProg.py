import sys
from ATMExcept import ZeroErr, NegativeErr, UnSuffWithdrawErr
from ATMOperation import DOp, WOp ,CbOp
from ATMOption import opt

while True:
    try:
        while True:
            opt()
            option = int(input("Enter Operation to be perform : "))
            match option:
                case 1:
                    try:
                        dm = float(input("Enter deposit Amount : "))
                        DOp(dm)
                    except ValueError:
                        print("Don't Enter Alpha/AlphaNum/SpecialSymbol")
                    except ZeroErr:
                        print("Don't Enter Zero OR Negative Number : ")
                    except NegativeErr:
                        print("Don't Enter Zero OR Negative Number : ")
                case 2:
                    try:
                        wm = float(input("Enter withdraw Amount : "))
                        WOp(wm)
                    except ValueError:
                        print("Don't Enter Alpha/AlphaNum/SpecialSymbol")
                    except ZeroErr:
                        print("Don't Enter Zero  ")
                    except NegativeErr:
                        print("Don't Enter Negative Number : ")
                    except UnSuffWithdrawErr:
                        print("UnSufficient Withdraw Amount : {}".format(v))
                case 3:
                    CbOp()
                case 4:
                    print("Thank you Come again")
                    sys.exit()
                case _:
                    print("--Invalid Option--")
    except ValueError:
        print("Don't Enter Alpha/AlphaNum/SpecialSymbol")
