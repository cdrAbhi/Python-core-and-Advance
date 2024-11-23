#ComprehensionEx2.py--dict comprehension
print("Enter List of Values of separatred by space for cal their squares:")
d= { int(val) : int(val)**2  for val in input().split()  }
print("set of Values={} and type={}".format(d,type(d)))


