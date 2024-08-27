fi = open("nopbai.inp", "r")
fo = open("nopbai.out", "w")
sn = fi.readline().split()
n = int(sn[0])
sa = fi.readline().split()
a = list()
for x in a:
    if (x < rmin):
        rmin = x
print(rmin, file_=_fo)