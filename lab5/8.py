import re
file = open('text.txt','r')
string = file.read()
print(re.findall('[A-Z][^A-Z]*',string))