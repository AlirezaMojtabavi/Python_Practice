import re

Email = str(input())
result = re.search(r'.+\@.+\..{2,3}', Email)

if result != None :
    print("OK")
else:
    print("WRONG")