#OppsApproachn02.py
import threading,time # step-I
# step-2     step-3
class Hyd(threading.Thread):
    def run(self): #step-4
        print("i am from run()")
        print("Therad based Application")
#main program
print("Name of main thread=",threading.current_thread().name)
h=Hyd() # here 'h' is an object of Hyd and considered as Child thread
print(f"execution status of h before start= {h.is_alive()}")
h.start()
print(f"execution status of h before start= {h.is_alive()}")
time.sleep(4)

