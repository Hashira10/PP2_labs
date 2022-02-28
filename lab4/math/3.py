import math
n = float(input("Input number of sides: "))
a = float(input("Input the length of a side: "))
print((n*a**2)/(4*math.tan(math.pi/n)))
