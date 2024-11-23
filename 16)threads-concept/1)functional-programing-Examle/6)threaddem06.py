# threaddem06.py
# write a thead based application which will generate a multiplication table by using threads(use funtional approach).
import threading,time
def mulTable(n):
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
        
        
# main program 
print(f"Number of active threads in this program before start: {threading.active_count()}")
n=int(input("Enter number :"))
t1=threading.Thread(target=mulTable,args=(n,))
print("Defult child thread",t1.name) # getting child thread name
t1.name="Hyd" # setting user-friendly thread name
print("Execution status of tl before start=",t1.is_alive()) # False(thread is not running )
t1.start()
print("Execution status of tl After start=",t1.is_alive()) # True(thread is running )
print(f"Number of active threads in this program after start : {threading.active_count()}")
t1.join()
print("Execution status of t1 after execution=",t1.is_alive()) # True(thread is running )
print(f"Number of active threads in this programafter after execution completion : {threading.active_count()}")




'''
outpu
=====
Number of active threads in this program before start: 1
Enter number :
12
Defult child thread Thread-1
Execution status of tl before start= False
Name of child thread = Hyd
**************************************************
	12x1 = 12
Execution status of tl After start= True
Number of active threads in this program after start : 2
	12x2 = 24
	12x3 = 36
	12x4 = 48
	12x5 = 60
	12x6 = 72
	12x7 = 84
	12x8 = 96
	12x9 = 108
	12x10 = 120
**************************************************
Execution status of t1 after execution= False
Number of active threads in this programafter after execution completion : 1


** Process exited - Return Code: 0 **
Press Enter to exit terminal
'''




        
