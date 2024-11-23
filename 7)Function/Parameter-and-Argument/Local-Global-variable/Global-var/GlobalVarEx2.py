#GlobalVarEx2.py
def learnAI():
    sub1="AI"
    print("To develop '{}' Applications, we use '{}' Lang ".format(sub1,lang))
    #print(sub2,sub3) here sub2 and sub3 are local in another fucntion Defs
def learnML( ):
    sub2 = "ML"
    print("To develop '{}' Applications, we use '{}' Lang ".format(sub2, lang))
    # print(sub1,sub3) here sub1 and sub3 are local in another fucntion Defs
def learnDL( ):
    sub3 = "DL"
    print("To develop '{}' Applications, we use '{}' Lang ".format(sub3, lang))
    # print(sub1,sub1) here sub1 and sub2 are local in another fucntion Defs
#main program
#learnAI()----we can't access 'lang' value bcoz it was defined after Function Call.
lang = "PYTHON" # Here lang is called Global Variable
learnML()
learnDL()