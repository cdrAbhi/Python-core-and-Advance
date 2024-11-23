#Program for generating char of a word or line of text
#WhileLoopEx4.py
line=input("Enter a word or line of text:")
i=0
while(i<=len(line)-1):
    print("\t\t\t{}".format(line[i]))
    i=i+1