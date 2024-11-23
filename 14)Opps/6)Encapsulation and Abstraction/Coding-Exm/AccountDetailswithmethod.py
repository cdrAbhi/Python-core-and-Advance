#AccountDetailswithmethod.py
class Account:
    def __getAccDet(self):
        self.acno = 100
        self.cname = "Rossum"
        self.bal = 5.6
        self.pin = 1234
        self.bname = "SBI-AMPT"
    def displayaccdet(self):
        self.__getAccDet() # Calling Encapsulated method Inside Instance Method in Same Class
        print("Account Number=", self.acno)
        print("Account Holder Name=", self.cname)
        print("Account Holder Bal=", self.bal)
        print("Account Holder Pin=", self.pin)
        print("Account Holder Branch Name=", self.bname)
#main program
ac=Account()
print(ac.__dict__)
#ac.__getAccDet() Not at all Possible to call bcoz we are in Main Program which is not a part of Class Context
ac.displayaccdet()