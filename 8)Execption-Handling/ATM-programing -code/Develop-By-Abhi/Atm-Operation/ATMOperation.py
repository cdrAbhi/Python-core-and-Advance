from ATMExcept import ZeroErr, NegativeErr, UnSuffWithdrawErr

cb = 525


def DOp(v):
    if v == 0:
        raise ZeroErr
    elif v < 0:
        raise NegativeErr
    else:
        global cb
        cb += v
        print("INR {} ₹ Successfully credited to your Account".format(v))
        print("Current Account Balance : {} ₹ ".format(cb))


def WOp(v):
    global cb
    if v == 0:
        raise ZeroErr
    elif v < 0:
        raise NegativeErr
    elif v > cb:
        raise UnSuffWithdrawErr
    else:
        cb -= v
        print("INR {} ₹ Successfully debited to your Account".format(v))
        print("Current Account Balance : {} ₹ ".format(cb))


def CbOp():
    print("Your current Account Balance is : {} ₹".format(cb))
