#MatchCaseEx4.py
wkn=input("Enter Week Name:")
match(wkn[0:3].upper()):
    case "MON"|"TUE"|"WED"|"THU"|"FRI":
        print("{} is Working Day".format(wkn))
    case "SAT":
        print("{} is Week-End--Preparing UGAP ".format(wkn))
    case "SUN":
        print("{} is HolyDay".format(wkn))
    case _:
        print("{} is Not weak day".format(wkn))