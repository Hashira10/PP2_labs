import re
file = open('text.txt','r')
string = file.read()
if re.search('ab*',string):
    print("Yes")
else:
    print("No")