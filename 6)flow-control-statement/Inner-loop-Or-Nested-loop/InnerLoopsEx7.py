#program for Generating  mul tables  for random values
#InnerLoopsEx7.py
lst=list() # empty list for storing random values
print("Enter List of Random Values and Press ! to stop:")
while(True):
    value=input()
    if(value=="!"):
        break
    lst.append(int(value))
print("List of Values:{}".format(lst)) 
#code of random numbers mul tables
for num in lst: # Outer Loop
    if(num<=0):
        print("{} is invalid input--can generate mul table".format(num))
        continue
    print("*"*50)
    print("Mul table for {}".format(num))
    print("*" * 50)
    for i in range(1,11): # inner Loop
        print("\t{} x {}={}".format(num,i,num*i))
    else:
        print("*" * 50)




