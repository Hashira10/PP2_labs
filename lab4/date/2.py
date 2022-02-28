import datetime
now = datetime.date.today()
yest = datetime.date.today() - datetime.timedelta(1)
tom = datetime.date.today() + datetime.timedelta(1)
print(now)
print(yest)
print(tom)