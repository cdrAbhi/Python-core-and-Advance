#threaddem05.py
# what are the purpose of join() function ?
# => purpose of join() is that join mainThread after completion of execution.

#program displaying 1 to 10 number after each and evevry second by using threads
#approachexl .py
import threading,time
def generate(n):
    print("Number of Numbers:{}".format(n))
    ctname=threading.current_thread().name
    print("Name of Child Thread=",ctname)
    print("*"*50)
    for i in range(1,n+1):
        print("\tValue of i={}".format(i))
        time.sleep(1)
    print("*"*50)    
#main porogram
mtname=threading.current_thread().name
print("Name of main thread={}".format(mtname))
t1=threading.Thread(target=generate, args=(10,) )#creating child thread
t1.name="Rossom"
t1.start() # distaching the child thread
print("Number of active threads=",threading.active_count())
t1.join()
print("Line24 Number of active threads=",threading.active_count()) # Here only mainThread available at the end child thread destroy by GC

'''
output
=====
Name of main thread=MainThread
Number of active threads= 2
Number of Numbers:10
Name of Child Thread= Rossom
**************************************************
	Value of i=1
	Value of i=2
	Value of i=3
	Value of i=4
	Value of i=5
	Value of i=6
	Value of i=7
	Value of i=8
	Value of i=9
	Value of i=10
**************************************************
Line24 Number of active threads= 1


** Process exited - Return Code: 0 **
Press Enter to exit terminal



'''

#tl .setName("Rs")