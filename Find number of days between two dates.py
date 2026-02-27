from datetime import date

# Date tuples (day, month, year)
date1 = (10, 2, 2024)
date2 = (21, 2, 2026)

d1 = date(date1[2], date1[1], date1[0])
d2 = date(date2[2], date2[1], date2[0])

difference = abs((d2 - d1).days)

print("Number of days between two dates:", difference)