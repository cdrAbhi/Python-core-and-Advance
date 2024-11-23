# Generator : Generator is method of generate value in function and supply it using yield if asked

def gen(s,e):
    # mth-1 to suply value
    # for value in range(s,e):
    #     yield value
    
    # Mthd-2 to supply value
    while s<e:
        yield s
        s+=1

d=gen(10,15) 
# print(type(d)) #d = is an object of <class 'generator'>

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
        
    