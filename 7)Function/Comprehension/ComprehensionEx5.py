#ComprehensionEx5.py
print("Enter List of Values of separatred by space:")
t= ( int(val)  for val in input().split()  )
tpl=tuple(t) # Type cast generator object into tuple type
print("Tuple of Values={} and type={}".format(tpl,type(tpl)))
