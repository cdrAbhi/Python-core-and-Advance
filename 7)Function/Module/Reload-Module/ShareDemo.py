#ShareDemo.py--Main Program
import Shares
import time,importlib
def disp(d):
    print("*"*50)
    print("ShareName\t\tShareValue")
    print("*" * 50)
    for sn,sv in d.items():
        print("\t{}----->{}".format(sn,sv))
    print("*" * 50)

#main program
d=Shares.sharesinfo()
disp(d)
print("I am going to sleep for 15 seonds")
time.sleep(15)
print("I am coming out-of sleep after 15 seonds")
importlib.reload(Shares)
d=Shares.sharesinfo()
disp(d)
print("I am going to sleep for 15 seonds")
time.sleep(15)
print("I am coming out-of sleep after 15 seonds")
importlib.reload(Shares)
d=Shares.sharesinfo()
disp(d)