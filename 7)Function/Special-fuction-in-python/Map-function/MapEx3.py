#MapEx3.py
print("Enter Equal Number of Values for First List:")
lst1=[int(val) for val in input().split()]
print("Enter Equal Number of Values for Second List:")
lst2=[int(val) for val in input().split()]
lst3=list(map(lambda x,y:x+y,lst1,lst2))
print("---------------------------------------------")
print("First List:{}".format(lst1))
print("Second List:{}".format(lst2))
print("Sum List:{}".format(lst3))
print("---------------------------------------------")