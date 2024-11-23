#AccountDetails.py
class Account:
    def getAccDet(self):
        self.__acno = 100
        self.cname = "Rossum"
        self.__bal = 5.6
        self.__pin = 1234
        self.bname = "SBI-AMPT"
    def displayaccdet(self):
        print("Account Number=", self.__acno)
        print("Account Holder Name=", self.cname)
        print("Account Holder Bal=", self.__bal)
        print("Account Holder Pin=", self.__pin)
        print("Account Holder Branch Name=", self.bname)
#main program
ac=Account()
ac.getAccDet()
ac.displayaccdet()