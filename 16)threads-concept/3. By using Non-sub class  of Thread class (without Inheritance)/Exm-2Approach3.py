#Exm-2Approach3.py
import threading,time
class MulTable:
    def gentable(self,n):
        tname=threading.current_thread().name
        print(f"Name of child thread = {tname}")
        if n<=0:
            print(f"Invalid Input : {n}")
        else:    
            print("*"*50)
            for i in range(1,11):
                print(f"\t{n}x{i} = {n*i}")
                time.sleep(1)
            print("*"*50)
            
#main program
print("Name of main thread=",threading.current_thread().name) # main thread
s=MulTable()
t1=threading.Thread(target=s.gentable,args=(5,))
t1.name="KVR"
t1.start()