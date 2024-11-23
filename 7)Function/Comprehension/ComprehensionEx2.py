#ComprehensionEx2.py--set comprehension
print("Enter List of Values of separatred by space:")
st= { int(val)  for val in input().split()  }
print("set of Values={} and type={}".format(st,type(st)))


