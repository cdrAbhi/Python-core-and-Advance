#Program for finding whether a value is alpha, digit or special symbols or alnum
#IfElseStmtEx3.py
val=input("Enter Any Value:")
if(val.isalpha()):
    print("'{} is an alphabet value".format(val))
else:
    if(val.isdigit()):
        print("'{} is an Digit value".format(val))
    else:
            if(val.isalnum()):
                print("'{} is an alpha-numeric value".format(val))
            else:
                print("'{}' is a special symbol".format(val))


