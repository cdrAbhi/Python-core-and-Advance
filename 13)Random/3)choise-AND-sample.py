import random

s="Ramaarajya"
l=[1,2,3,4,5,6]
for i in range(5):
    print(random.choice(s),random.choice(l))
    
for i in range(5):
    print(random.sample(s,k=len(l)))
    
    
'''====output====
a 6
r 4
j 6
a 2
y 4
['j', 'a', 'a', 'a', 'r', 'a']
['R', 'm', 'a', 'a', 'a', 'a']
['a', 'r', 'a', 'j', 'y', 'm']
['a', 'a', 'r', 'y', 'a', 'a']
['a', 'R', 'a', 'y', 'a', 'r']


** Process exited - Return Code: 0 **
Press Enter to exit terminal

'''