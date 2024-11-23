#Program will display to n numbers by using threads with OOPs (Inheritance)
#NumGenEx1.py
import time
from threading import Thread

class Numbers(Thread):
    def run(self): # Overridden run()
        self.n=int(input("Enter Number of Numbers to generate: "))
        if(self.n<=0):   
            print("O is invalid input:".format(self.n))
        else:
            print(f"Number within:{self.n}")
            for i in range(1,self.n+1):
                print("\tVal of i={}".format(i))
                time.sleep(1)
#main program
n=Numbers() # creating child thread
n.start()