#Program for Demonstrating keyword Variable length args
#This Program will  execute as it is 
#KwdVarlenArgsEx2.py
def disp(sno,sname,cm,cpp,py): # Function Def-1
	print(sno,sname,cm,cpp,py)
disp(sno=10,sname="RS",cm=40,cpp=50,py=60) # Function call-1--with 5 Kwd Var length args
#--------------------------------------------------------------------------
def disp(eno,ename,hb1,hb2,hb3,hb4):
	print(eno,ename,hb1,hb2,hb3,hb4)

disp(eno=100,ename="Ravi",hb1="Hungry",hb2="Sleep",hb3="Good",hb4="Reading") # Function call-2 with 6 kwd  var length args
#--------------------------------------------------------------------------
def disp(a,b,c,d):
	print(a,b,c,d)
disp(a=10,b=20,c=30,d=40) # Function call-3 with 4 kwd  var length args
#--------------------------------------------------------------------------
def disp(tno,tname):
	print(tno,tname)
disp(tno=1000,tname="KV") # Function call-4 with 2 kwd  var length args
#--------------------------------------------------------------------------
def  disp(bno):
	print(bno)
disp(bno="BID234") # Function call-5 with 1 kwd  var length args
#--------------------------------------------------------------------------





