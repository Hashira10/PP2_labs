import re
file = open('text.txt','r')
string = file.read()
if re.search(r'[a-z]\S*_\S*[a-z]',string):
    print("Yes")
else:
    print("No")