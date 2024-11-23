#lockingex3.py
====================

import threading,time 

class MulTab:
    @classmethod
    def getlockobj(cls):
        cls.L=threading.Lock()
    
    def __init__(self,n):
        self.n=n
        
    def getMul(self):
        self.L.acquire() # step-2
        print("Child Thread Name=",threading.current_thread().name)
        print("MulTable for {}".format(self.n))
        for i in range(1,11):
            print(f"{self.n}x{i}={self.n*i}") 
            time.sleep(1)
        self.L.release() # Step-3
        
#main program
MulTab.getlockobj()
m1=MulTab(2)
m2=MulTab(3)
m3=MulTab(4)
#create multiple child threads
t1=threading.Thread(target=m1.getMul)
t2=threading.Thread(target=m2.getMul)
t3=threading.Thread(target=m3.getMul)
#dispatch the therads
t1.start()
t2.start()
t3.start()

'''
output
=======
Child Thread Name= Thread-1
MulTable for 2
2x1=2
2x2=4
2x3=6
2x4=8
2x5=10
2x6=12
2x7=14
2x8=16
2x9=18
2x10=20
Child Thread Name= Thread-2
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
Child Thread Name= Thread-3
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


** Process exited - Return Code: 0 **
Press Enter to exit terminal
'''