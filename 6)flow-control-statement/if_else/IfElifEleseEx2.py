#Program for accepting any digit and display its name
#IfElifEleseEx2.py
dobj={0:"ZERO",1:"ONE",2:"TWO",3:"THREE",4:"FOUR",5:"FIVE",6:"SIX",7:"SEVEN",8:"EIGHT",9:"NINE",-1:"-ONE",-2:"-TWO",-3:"-THREE",-4:"-FOUR",-5:"-FIVE",-6:"-SIX",-7:"-SEVEN",-8:"-EIGHT",-9:"-NINE",}
d=int(input("Enter Ur Digit:"))
res=dobj.get(d)  if dobj.get(d)!=None  else " is +Number" if d>0 else " is -Ve Number"
print("{} is {}".format(d,res))