#MatchCaseEx2.py
wkn=input("Enter Week Name:")
match(wkn.upper()):
    case "MONDAY":
        print("{} is Working Day".format(wkn))
    case "TUESDAY":
        print("{} is Working Day".format(wkn))
    case "WEDNESDAY":
        print("{} is Working Day".format(wkn))
    case "THURSDAY":
        print("{} is Working Day".format(wkn))
    case "FRIDAY":
        print("{} is Working Day".format(wkn))
    case "SATURDAY":
        print("{} is Week-End--Preparing UGAP ".format(wkn))
    case "SUNDAY":
        print("{} is HolyDay".format(wkn))
    case _:
        print("{} is Not weak day".format(wkn))