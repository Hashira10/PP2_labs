import re
file = open('text.txt','r')
string = file.read()
words = re.findall(r"([a-z]+)\_*",string)
print("".join(i.capitalize() for i in words))
'''
string = input()
new_str = string.split("_")
s = ""
for i in new_str:
    s+=i.capitalize()
print(s)
'''