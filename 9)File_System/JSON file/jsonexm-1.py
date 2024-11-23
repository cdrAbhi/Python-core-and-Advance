import json
jd='{"Name":"Abhishek","Age":"21","Study":"B.E"}'
print(type(jd))
d=json.loads(jd)
# print(d)
for k in d:
    print(f"{k}-->{d[k]}")