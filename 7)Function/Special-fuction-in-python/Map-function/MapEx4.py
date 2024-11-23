#MapEx4.py
print("Enter  Number of Values for First List:")
lst1=[int(val) for val in input().split()]
print("Enter  Number of Values for Second List:")
lst2=[int(val) for val in input().split()]
if(len(lst1)>len(lst2)):
    for i in range(len(lst1)-len(lst2)):
        lst2.append(0)
elif(len(lst2)>len(lst1)):
    for i in range(len(lst2)-len(lst1)):
        lst1.append(0)
#now add the Elements of lst1 and lst2
lst3=list(map(lambda a,b: a+b,lst1,lst2))
print("---------------------------------------------")
print("First List:{}".format(lst1))
print("Second List:{}".format(lst2))
print("Sum List:{}".format(lst3))
print("---------------------------------------------")


