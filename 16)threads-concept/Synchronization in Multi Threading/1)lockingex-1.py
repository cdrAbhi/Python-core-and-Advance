#lockingexl.py
import threading , time
k=threading.Lock() # Step-I
def multable(n):
    k.acquire() # step-2
    print("Child Thread Name=",threading.current_thread().name)
    print("MulTable for {}".format(n))
    for i in range(1,11):
        print(f"{n}x{i}={n*i}") 
        time.sleep(1)
    k.release() # Step-3
#main program
t1=threading.Thread(target=multable,args=(5,))
t2=threading.Thread(target=multable,args=(13,))
t3=threading.Thread(target=multable,args=(27,))
t1.start()
t2.start()
t3.start()