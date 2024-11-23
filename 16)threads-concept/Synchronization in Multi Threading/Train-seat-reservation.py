# Train-seat-reservation.py

import threading
class Train:
    L=threading.Lock()
    def __init__(self):
        self.seats=20
    def reservation(self,nos):
        self.L.acquire()
        if(nos>self.seats):
            print("{} unable get {} seats:".format(threading.current_thread().name, nos))
        else:
            self.seats=self.seats-nos
            print("{} Reserved {} seats:".format(threading.current_thread().name, nos))
        self.L.release()
        
#main program
t=Train()
t1=threading.Thread(target=t.reservation, args=(10,))
t2=threading.Thread(target=t.reservation, args=(15,))
t3=threading.Thread(target=t.reservation, args=(23,))
#dispatch the threads 
t1.start()
t2.start()
t3.start()

'''

output
========
Thread-1 Reserved 10 seats:
Thread-2 unable get 15 seats:
Thread-3 unable get 23 seats:


** Process exited - Return Code: 0 **
Press Enter to exit terminal
'''