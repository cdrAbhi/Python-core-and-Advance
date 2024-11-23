#InnerLoopsEx5.py
for i in range(1,4):
    print("=======================")
    print("\t\ti\tj\tk")
    for j in range(1,4):
        for k in range(1,4):
            print("\t\t{}\t{}\t{}".format(i,j,k))
        else:
            print("-----------------------------")
    else:
        print("=======================")