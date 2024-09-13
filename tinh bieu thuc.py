from math import *
file = open("ROOT.INP")
file2 = open("ROOT.OUT","w")
a = file.readline()
b = file.readline()
c = file.readline()
a = int(a)
b = int(b)
c = int(c)
tu = a**2 + b**2 + c**2
mau = a * b * c
s = tu/mau + sqrt(mau)
s = str(round(s,2))

file2.write(s)
file.close()
file2.close()
print(s)