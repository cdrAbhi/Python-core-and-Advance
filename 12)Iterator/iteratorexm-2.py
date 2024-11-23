# Iterator : Iterator is method of generate Iterator Object by enter arguent as a iterableObject to iter() and supply value of it if asked or demand.

# b,e,s=input("Enter begin :"),input("Enter end :"),input("Enter step :")
b,e,s=2,10,2
iterobj = iter(i for i in range(b,e,s))

# print(type(iterobj)) #d = is an object of <class 'list_iterator'>

# mthd-1 get value
# ---how to get one value at a time-----------------------------------------------
print(next(iterobj),next(iterobj),next(iterobj))
# print(next(iterobj))      #==> try to get value out of range raise StopIteration Exception
# --------------------------------------------------

# mthd-2 get value
# ---how to get all value one by one along with handle raise StopIteration Exception-----------------------------------------------
# while True:
#     try:
#         print(next(iterobj))
#     except StopIteration: 
#         break
# --------------------------------------------------

# mthd-3 get value
# ---------------------------------------------------
lstval=list(v for v in iterobj)
i=0
# we can print value of list while or for loop.
# mthd-1
# ========= 
# while True:
#     if i==len(lstval): 
#         break
#     else:
#         print(lstval[i])
#         i+=1

# mthd-1
# ========
# while True:
#     if i<len(lstval): 
#         print(lstval[i])
#         i+=1
#     else:
#         break

# mthd-3
# ======
# while True:
#     try:
#         print(lstval[i])
#         i+=1
#     except IndexError:
#         break
    
# ----------------------------------------------------
        
    
# mthd-1 get value
# ---how to get one value at a time-----------------------------------------------
# print(next(d),next(d),next(d),next(d),next(d))
# print(next(d))      #==> try to get value out of range raise StopIteration Exception
# --------------------------------------------------

# mthd-2 get value
# ---how to get all value one by one along with handle raise StopIteration Exception-----------------------------------------------
# while True:
#     try:
#         print(next(d))
#     except StopIteration: 
#         break
# --------------------------------------------------

# mthd-3 get value
# ---------------------------------------------------
# lstval=list(v for v in d)
# i=0
# we can print value of list while or for loop.
# mthd-1
# ========= 
# while True:
#     if i==len(lstval): 
#         break
#     else:
#         print(lstval[i])
#         i+=1

# mthd-1
# ========
# while True:
#     if i<len(lstval): 
#         print(lstval[i])
#         i+=1
#     else:
#         break

# mthd-3
# ======
# while True:
#     try:
#         print(lstval[i])
#         i+=1
#     except IndexError:
#         break
    
# ----------------------------------------------------
        
    