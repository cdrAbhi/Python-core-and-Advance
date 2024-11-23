#FilterFunEx6.py
line=input("Enter a Line of Text:") # line=Sky is Blue and why not Black
vowwords=list(filter(lambda word: word.isalpha() and 'a' in word.lower() or 'e' in word.lower() or 'i' in word.lower() or 'o' in word.lower() or 'u' in word.lower(), line.split()))
conswords=list(filter(lambda word:word.isalpha() and 'a' not in word.lower() and 'e' not in word.lower() and 'i' not in word.lower() and 'o' not in word.lower() and 'u' not in word.lower(), line.split()))
print("Given Line of Text:{}".format(line))
print("Vowel Words={}".format(vowwords))
print("Cons. Words={}".format(conswords))