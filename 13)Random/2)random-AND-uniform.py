import random
print("--random()-------------print float value in between 0 to 1")
for i in range(1,6):
    print(random.random())
    
print("--uniform(1,3)--------------print float value in range begin to end-1")    
for i in range(1,10):   
    print(random.uniform(1,3))




''' ===output====
--random()-------------print float value in between 0 to 1
0.8653550419645497
0.9671214160665104
0.5040057547418404
0.19261502820932774
0.8751360984360886
--uniform(1,3)--------------print float value in range begin to end-1
1.5597867614944019
1.466033887778158
1.8676302103867364
2.8147227639399426
1.3267398556082959
2.717385658790221
1.2239232042450932
1.7128402448608877
1.6643462493256391


** Process exited - Return Code: 0 **
Press Enter to exit terminal
'''