#Program for accepting any digit and display its name
#IfElseStmtEx4.py
d=float(input("Enter any digit:")) # 0 1  2  3 4 5 6 7 8 9
if(d==0.0):
    print("{} is ZERO".format(d))
else:
    if(d==1.0):
        print("{} is ONE".format(d))
    else:
        if(d==2.0):
            print("{} is TWO".format(d))
        else:
            if(d==3.0):
                print("{} is THREE".format(d))
            else:
                if(d==4.0):
                    print("{} is FOUR".format(d))
                else:
                    if(d==5.0):
                        print("{} is FIVE".format(d))
                    else:
                        if(d==6.0):
                            print("{} is SIX".format(d))
                        else:
                            if(d==7.0):
                                print("{} is SEVEN".format(d))
                            else:
                                if(d==8.0):
                                    print("{} is EIGHT".format(d))
                                else:
                                    if(d==9.0):
                                        print("{} is NINE".format(d))
                                    else:
                                        if (d == -1.0):
                                            print("{} is -ONE".format(d))
                                        else:
                                            if (d == -2.0):
                                                print("{} is -TWO".format(d))
                                            else:
                                                if (d == -3.0):
                                                    print("{} is -THREE".format(d))
                                                else:
                                                    if (d == -4.0):
                                                        print("{} is -FOUR".format(d))
                                                    else:
                                                        if (d == -5.0):
                                                            print("{} is -FIVE".format(d))
                                                        else:
                                                            if (d ==-6.0):
                                                                print("{} is -SIX".format(d))
                                                            else:
                                                                if (d == -7.0):
                                                                    print("{} is -SEVEN".format(d))
                                                                else:
                                                                    if (d == -8.0):
                                                                        print("{} is -EIGHT".format(d))
                                                                    else:
                                                                        if (d == -9.0):
                                                                            print("{} is -NINE".format(d))
                                                                        else:
                                                                            if(d not in [0,1,2,3,4,5,6,6,7,8,9] and d>=0):
                                                                                print("{} is +Ve Number".format(d))
                                                                            else:
                                                                                print("{} is -Ve Number".format(d))
