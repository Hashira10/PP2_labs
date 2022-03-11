import re
file = open('text.txt','r')
string = file.read()
if re.findall('[A-Z]+[a-z]+',string):
    print("Yes")
else:
    print("No")