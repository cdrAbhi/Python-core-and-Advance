# nonlockinge.py
import threading , time
k=threading.Lock()
def multable(n):
    print("Child Thread Name=",threading.current_thread().name)
    print("Mul Table for O ".format(n))
    for i in range(1,11):
        print(f"{n}x{i}={n*i}") 
        # time.sleep(1)
#main program
t1=threading.Thread(target=multable,args=(2,))
t2=threading.Thread(target=multable,args=(3,))
t3=threading.Thread(target=multable,args=(4,))
t1.start()
t2.start()
t3.start()