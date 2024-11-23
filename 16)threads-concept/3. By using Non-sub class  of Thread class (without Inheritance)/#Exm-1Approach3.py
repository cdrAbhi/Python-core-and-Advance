#Exm-1Approach3.py
import threading
class Sample:
    def show(self):
        print("Name of child thread=",threading.current_thread().name) # Thread-I
        print("show() of Sample")
        print("We write thread based logic")
        
#main program
print("Name of main thread=",threading.current_thread().name) # main thread
s=Sample()
t1=threading.Thread(target=s.show)
t1.name="KVR"
t1.start()