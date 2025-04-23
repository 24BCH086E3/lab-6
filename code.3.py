from datetime import date

date1 = (20, 4, 2025)
date2 = (1, 1, 2025)
d1 = date(date1[2], date1[1], date1[0])
d2 = date(date2[2], date2[1], date2[0])
delta = abs((d1 - d2).days)
print("Number of days between dates:", delta)
