# -*- coding:utf-8 -*-

# with open('file', encoding='utf-8') as f:
#     lines = (line.strip() for line in f)
#     for line in lines:
#         print(line)


from datetime import timedelta, datetime

a = timedelta(days=3, hours=6)
b = timedelta(hours=4.5)
c = a + b
print(c.days)
print(c.seconds)
print(c.seconds / 3600)
print(c.total_seconds() / 3600)

d = datetime(2012, 9, 23)
print(d + timedelta(days=10))
print(datetime.today())
