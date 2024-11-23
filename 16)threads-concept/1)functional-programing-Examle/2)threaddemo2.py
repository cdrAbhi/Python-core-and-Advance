#threaddemo2.py
import threading
def Hello():
    tname1 =threading.current_thread().name
    print(f"\nHello() executed by {tname1}" )
    print("i am from hello()")
def Hi():
    tname2=threading.current_thread().name
    print(f"\nHi() executed by {tname2}" )
    print("i am from Hi()")
def Show():
    tname3 =threading.current_thread().name
    print(f"\nShow() executed by {tname3}" )
    print("i am from Show()")
    
#main program
dftname=threading.current_thread().name
print(f"\ndefault Name of thread in main program={dftname}")
Hello()
Hi()
Show()    