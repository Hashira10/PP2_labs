import os
first = open("test.txt",'r')
second = open("text2.txt", 'a')
for i in first:
    second.write(i)