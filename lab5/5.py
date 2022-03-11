import re
file = open('text.txt','r')
string = file.read()
if re.findall('a.*?b$',string):
    print("Yes")
else:
    print("No")