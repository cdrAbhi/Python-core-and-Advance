# write a python program which will accept a numerical interger value and genrate multiplication table of it.
"""
====================================================================================
NOte:
====
Below are operation only done inside method not on the class level..
    obj=value()
    obj.getval()
    MulTable.getMulTable(obj)   
======================================================================================
"""
# wrong approach - 1
# ===================

# class value:
#     def getval(self):
#         self.val=int(input("Enter integer value : "))

# class MulTable:
#     obj=value()
#     obj.getval()
#     MulTable.getMulTable(obj)
#     @staticmethod
#     def getMulTable(obj):
#         for i in range(1,11):
#             print(f"{obj.val}x{i} = {obj.val*i}")
            

       
# Mulobj=MulTable()     


# =========================
# wrong approach-2
# ============================
# class MulTable:
#     val()
#     @staticmethod
#     def getMulTable(obj):
        
#         for i in range(1,11):
#             print(f"{obj.val}x{i} = {obj.val*i}")
#         else:
#             print(obj.__dict__)
            
# class value:
#     def getval(self):
#         self.val=int(input("Enter integer value : "))

# obj=value()
# val=obj.getval
# Mulobj=MulTable()  
# Mulobj.getMulTable(obj)
# =================================



# correct aproch of create a object inside a class of other class is by using methods(instance or statics or classlevel) or decorator
# =================================================================================================
# mthd-1
# ========
# class Value:
#     def get_val(self):
#         self.val = int(input("Enter an integer value: "))

# class MulTable:
#     def __init__(self):
#         self.obj = Value()
#         self.obj.get_val()
#         self.get_mul_table()

#     def get_mul_table(self):
#         for i in range(1, 11):
#             print(f"{self.obj.val} x {i} = {self.obj.val * i}")

# # Create an instance of MulTable to run the program
# mul_obj = MulTable()


# method-2
# ============
# # write a python program which will accept a numerical interger value and genrate multiplication table of it.

# class MulTable:
#     @classmethod
#     def startop(cls):
#         obj=value()
#         obj.getval()
#         MulTable.getMulTable(obj)
#     @staticmethod
#     def getMulTable(obj):
#         for i in range(1,11):
#             print(f"{obj.val}x{i} = {obj.val*i}")
            
# class value:
#     def getval(self):
#         self.val=int(input("Enter integer value : "))
        
# MulTable.startop()  

# ====================


        
            