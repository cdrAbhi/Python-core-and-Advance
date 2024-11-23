#MatchCaseEx3.py
wkn=input("Enter Week Name:")
match(wkn.upper()):
    case "MONDAY"|"TUESDAY"|"WEDNESDAY"|"THURSDAY"|"FRIDAY":
        print("{} is Working Day".format(wkn))
    case "SATURDAY":
        print("{} is Week-End--Preparing UGAP ".format(wkn))
    case "SUNDAY":
        print("{} is HolyDay".format(wkn))
    case _:
        print("{} is Not weak day".format(wkn))