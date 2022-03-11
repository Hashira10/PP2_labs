import re
file = open('text.txt','r')
string = file.read()
words = re.sub(r"(\w)([A-Z])", r"\1 \2",string)
print(words)