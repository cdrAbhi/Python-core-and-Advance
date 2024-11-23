#program for accepting Two Integer Values and find their Div without handling the exceptions
#Div1.py
s1=input("Enter First Value:")
s2=input("Enter Second Value:")
a=int(s1)    #  Exception generated statement----ValueError
b=int(s2)  #  Exception generated statement----ValueError
print("First Value:{}".format(a))
print("Second Value:{}".format(b))
c=a/b   #  Exception generated statement----ZeroDivisionError
print("Div={}".format(c))
