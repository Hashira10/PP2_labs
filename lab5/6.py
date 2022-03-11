import re
file = open('text.txt','r')
string = file.read()
print(re.sub('[ ,.]',':',string))