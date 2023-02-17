import datetime
from datetime import datetime, time, timedelta, date
# task 1
# dt = date.today() - timedelta(0)
# print('Current Date :',date.today())
# print('5 days before Current Date :',dt)

# task 2
# dt = date.today()
# dy = date.today() - timedelta(1)
# dt2 = date.today() + timedelta(1)
# print(dy, dt, dt2)

# task 3

# print(datetime.datetime.today().replace(microsecond = 0))

# task 4

# dt1 = datetime.strptime("2020-02-15 02:45:51", "%Y-%m-%d %H:%M:%S")
# dt2 = datetime.now()
# timedelta1 = dt2 - dt1
# df = timedelta1.days * 24 * 3600 + timedelta1.seconds
# print("\n%d seconds"%df)