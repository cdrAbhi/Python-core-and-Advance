#ComprehensionEx6.py--list comprehension
print("Enter List of Values of separatred by space:")
pslst= [ int(val)  for val in input().split()    if int(val)>0  ]
print("Enter List of Values of separatred by space:")
nslst= [ int(val)  for val in input().split()    if int(val)<0  ]
print("List of +Ve Values={}".format(pslst))
print("List of -Ve Values={}".format(nslst))




