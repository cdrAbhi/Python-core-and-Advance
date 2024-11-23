#ComprehensionEx9.py--list comprehension
print("Enter List of Values of separatred by space:")
lst= [ int(val)  for val in input().split()  if int(val)>0 and int(val)%2==0 ]
print("List of +ve Even Values={}".format(lst))


