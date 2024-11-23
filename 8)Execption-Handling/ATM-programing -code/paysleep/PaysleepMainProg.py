from PaysleepExcept import ZeroErr, NegativeErr, UserNameErr
from PaysleepGeneratOperation import spl
import sys

try:
    while True:
        print(
            """
        Enter Option 
        ============
        1.Continue process
        2.Exit
        ===========
        """)
        op = int(input("Option : "))
        match op:
            case 1:
                try:
                    n = int(input("Enter your Employ Number : "))
                    s = int(input("Enter your Salary : "))
                    u = input("Enter your Name : ")
                    spl(n,s,u)
                except ValueError:
                    print("Don't Enter Alpha/AlphaNum/SpecialSymbol")
                except ZeroErr:
                    print("Don't Enter Zero : ")
                except NegativeErr:
                    print("Don't Enter Negative Number : ")
                except UserNameErr:
                    print("Invalid User Name ")
                except:
                    print("Invalid input")
            case 2:
                print("== Thank your for using this program ==")
                sys.exit()
            case _:
                print("{} is Invalid Option".format(op))
except ValueError:
    print("Don't Enter Alpha/AlphaNUm/Float/")
