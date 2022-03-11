import re
file = open('text.txt','r')
string = file.read()
words = re.findall('([A-Z][a-z]+)',string)
k = "_".join(i[:1].lower()+i[1:] for i in words)
print(k)
