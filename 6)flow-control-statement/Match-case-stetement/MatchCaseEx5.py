#MatchCaseEx5.py
wkn=input("Enter Week Name:")
if wkn.upper() in ["MON","TUE","WED","THU","FRI","SAT","SUN","MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY"]:
    match(wkn[0:3].upper()):
        case "MON"|"TUE"|"WED"|"THU"|"FRI":
            print("{} is Working Day".format(wkn))
        case "SAT":
            print("{} is Week-End--Preparing UGAP ".format(wkn))
        case "SUN":
            print("{} is HolyDay".format(wkn))
else:
    print("{} is Not weak day".format(wkn))