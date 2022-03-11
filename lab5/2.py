import re
file = open('text.txt','r')
string = file.read()
if re.search('ab{2,3}',string):
    print("Yes")
else:
    print("No")