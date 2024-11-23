from PaysleepExcept import ZeroErr, NegativeErr, UserNameErr


def spl(n, s, u):
    ls = list(u.split())
    for v in ls:
        if not v.isalpha():
            raise UserNameErr

    else:
        if n == 0 or s == 0:
            raise ZeroErr
        elif n < 0 or s < 0:
            raise NegativeErr
        elif s >= 10000:
            print("\tpayslip of Employee Number : ".format(n))
            print("*" * 50)
            print("\tEmployee Name : {}".format(u))
            print("-" * 50)
            print("\tda = {}".format(s * 0.2))
            print("\tta = {}".format(s * 0.1))
            print("\tcca = {}".format(s * 0.03))
            print("\tma = {}".format(s * 0.02))
            print("\thra= {}".format(s * 0.12))
            print("\tDeductions")
            print("\tlic= {}".format(s * 0.02))
            print("\tgpf= {}".format(s * 0.02))
            print("*" * 50)
            print("\tNetSal : {}".format(
                (s + (s * 0.2 + s * 0.1 + s * 0.03 + s * 0.02 + s * 0.12)) - (s * 0.02 + s * 0.02)))
        else:
            print("\tpaysleep of Employee Number : ".format(n))
            print("*" * 50)
            print("\tEmployee Name : {}".format(u))
            print("-" * 50)
            print("\tda = {}".format(s * .18))
            print("\tta = {}".format(s * 0.07))
            print("\tcca = {}".format(s * 0.02))
            print("\tma = {}".format(s * 0.02))
            print("\thra= {}".format(s * 0.08))
            print("\tDeductions")
            print("\tlic= {}".format(s * 0.01))
            print("\tgpf= {}".format(s * 0.015))
            print("*" * 50)
            print("\tNetSal : {}".format(
                (s + (s * 0.18 + s * 0.07 + s * 0.02 + s * 0.02 + s * 0.08)) - (s * 0.01 + s * 0.015)))
