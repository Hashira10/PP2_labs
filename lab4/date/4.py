import datetime
d1 = datetime.datetime.now()
d2 = datetime.datetime(2022,2,28,20,30,4)
dif = d1 - d2
print(dif.total_seconds())