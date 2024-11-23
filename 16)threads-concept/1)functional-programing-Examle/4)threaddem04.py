#threaddem04.py
import time
import threading
def squares(lst):
    tname1=threading.current_thread().name
    print(f"\nsqaures() executed by {tname1}")
    for val in lst:
        print(f"square({val})={val**2}")
        time.sleep(1)
        
def cubes(lst):
    tname2=threading.current_thread().name
    print(f"\ncubes() executed by {tname2}")
    for val in lst:
        print(f"square({val})={val**2}")
        time.sleep(1)


#main program
bt=time.time()
dftname=threading.current_thread().name
print(f"\ndefault Name of thread in main Program = {dftname}")
lst=[1,2,3,4,5,6,7,8]
st1=threading.Thread(target=squares,args=(lst,) ) # creating child thread
rt1 =threading.Thread(target=cubes,args=(lst,) )# creating child thread
#send child threads to execute functions
st1.start()
rt1.start()
st1.join()
rt1.join()
et=time.time()
print(f"\nExecution of time non-threading Application total time takng = {et-bt}")


''' output

default Name of thread in main Program = MainThread

sqaures() executed by Thread-1
square(1)=1

cubes() executed by Thread-2
square(1)=1
square(2)=4
square(2)=4
square(3)=9
square(3)=9
square(4)=16
square(4)=16
square(5)=25
square(5)=25
square(6)=36
square(6)=36
square(7)=49
square(7)=49
square(8)=64
square(8)=64

Execution of time non-threading Application total time takng = 8.018028020858765


** Process exited - Return Code: 0 **
Press Enter to exit terminal

'''