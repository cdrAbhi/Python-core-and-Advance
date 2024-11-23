#write a python programmer which will validate name of the person or place by using the following validate
    #if name contains number and special symbol then raise exception the name must be purelly alphabet
# =================================================================================================
from StrExp import AlpNumErr
try:
    v=input("Enter value: ")
    if not v.isalpha():
        raise AlpNumErr
except AlpNumErr:
    print("Don't Enter Alphanum/Digit/special Symbol")
else:
    print("Enter value : {}".format(v))
    