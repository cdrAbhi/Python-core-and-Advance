# lockingex2.py
# ==============
import threading,time 

class mulTable(threading.Thread):
    k=threading.Lock()
    def setval(self,n):
        self.n=n 
        self.getMul()
    def getMul(self):
        self.k.acquire() # step-2
        print("Child Thread Name=",threading.current_thread().name)
        print("MulTable for {}".format(self.n))
        for i in range(1,11):
            print(f"{self.n}x{i}={self.n*i}") 
            time.sleep(1)
        self.k.release() # Step-3
        
        
#main program
t1=mulTable()
t2=mulTable()
t3=mulTable()
t1.setval(5)
t2.setval(4)
t3.setval(3)
t1.start()
t2.start()  
t3.start()
        
'''
Output
=======
Child Thread Name= MainThread
MulTable for 5
5x1=5
5x2=10
5x3=15
5x4=20
5x5=25
5x6=30
5x7=35
5x8=40
5x9=45
5x10=50
Child Thread Name= MainThread
MulTable for 4
4x1=4
4x2=8
4x3=12
4x4=16
4x5=20
4x6=24
4x7=28
4x8=32
4x9=36
4x10=40
Child Thread Name= MainThread
MulTable for 3
3x1=3
3x2=6
3x3=9
3x4=12
3x5=15
3x6=18
3x7=21
3x8=24
3x9=27
3x10=30


'''
