#Program for generating char of a word or line of text
#WhileLoopEx5.py
import time
line=input("Enter a word or line of text:")
i=-len(line)
while(i<=-1):
    print("\t\t\t{}".format(line[i]))
    i=i+1
    time.sleep(1)