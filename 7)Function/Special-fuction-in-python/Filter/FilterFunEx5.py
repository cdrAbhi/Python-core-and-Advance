#FilterFunEx5.py
line=input("Enter a Line of Text:") # line=Apple is in red
vowlist=list(filter(lambda word: 'a' in word.lower() or 'e' in word.lower() or 'i' in word.lower() or 'o' in word.lower() or 'u' in word.lower(), line))
print("Given Line={}".format(line))
print("Vowels List={}".format(vowlist))