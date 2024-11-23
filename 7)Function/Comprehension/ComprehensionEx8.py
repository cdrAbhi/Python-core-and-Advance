#ComprehensionEx8.py
print("Enter list of words separated by comma ")
wordlen={word:len(word)  for word in input().split(",")  if (word==word[::-1]) }
if(len(wordlen)):
    print("List of Palindrome words and their length")
    for key,val in wordlen.items():
        print("\t{}-->{}".format(key,val))
else:
    print("No Palindrome words Found")