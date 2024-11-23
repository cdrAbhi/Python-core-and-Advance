#ComprehensionEx1.py--list comprehension
print("Enter List of Values of separatred by space:")
lst= [ int(val)  for val in input().split()  ]
print("List of Values={} and type={}".format(lst,type(lst)))


