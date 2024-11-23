#Program for Demonstrating GC running or Not
#GCEX1.py
import gc
print("Program Execution Started")
print("\tIntially, Is GC Running=", gc.isenabled())  # True
a=10
b=20
gc.disable()
print("Val of a=",a)
print("Val of b=",b)
print("\tNow Is GC Running after disable()=", gc.isenabled())  # False
c=a+b
gc.enable()
print("sum=",c)
print("\tNow Is GC Running after enable() =", gc.isenabled())  # True
print("Program Execution Started")




