from NumExe import ZeroErr,NegativeErr
def mulTbl(n):
    if n==0:
        raise ZeroErr
    elif n<0:
        raise NegativeErr
    else:
        print("======multiplicatin Table of {}====".format(n))
        for i in range(1,11):
            print("\t{}x{} = {}".format(n,i,n*i))