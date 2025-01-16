import sys
locations= sys.path
print(locations)

for i in locations:
    print(i)

import calendar

leapdays=calendar.leapdays(2000,2050)
print(leapdays)
esBisiesto=calendar.isleap(2028)
print(esBisiesto)