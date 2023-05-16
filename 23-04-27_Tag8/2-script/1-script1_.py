print('------#1  calaendar.isleap()-----')
print()

import calendar
calendar.isleap(2024)

my_year = 2024

if calendar.isleap(my_year):
    print(f'Year {my_year} is a leap year')
else:
    print(f'Year {my_year} is not a leap year')


print('--------------------------------')
print()
print()

# alternative codes: nochmal überlegen
#print('yes' if calendar.isleap(my_year) else 'No')

#result =(f'Year {my_year} is a leap year' if calendar.isleap(my_year) else f'Year {my_year} is not a leap year')
#print(result)

print('--------------------------------')
print()
print()




# oder mit Frage an User (eigener code):

print('Wir checken, ob ein Schaltjahr vorliegt!')
print('=======================================')

my_year = int(input("Gib eine Jahreszahl ein: "))

import calendar
calendar.isleap(my_year)

if calendar.isleap(my_year):
    print(f'==> Year {my_year} ist tatsächlich ein Schaltjahr!! =) ')
else:
    print(f'==> Year {my_year} ist leider kein Schaltjahr =C )')



###########################
print()
print()





print('------#2 month method -----')

import calendar
print(calendar.month(2022, 12))


# costomizing
calendar.setfirstweekday(1)
print(calendar.month(2022, 12))   # gibt schönen stanni cal aus

calendar.setfirstweekday(calendar.WEDNESDAY)
print(calendar.month(2022, 12))   

calendar.firstweekday()   # number of the first weekday of this month we setted

# each weekday is number between 0-6 and are dored in calendar.WEEKDAY
calendar.MONDAY    # 1
calendar.SUNDAY    # 6


print('------#3  ---ARITHMENTICS WITH DAYTIME--')
from datetime import datetime
halloween2019 = datetime(2019, 10, 31)
print(halloween2019)

oct31_2019 = datetime(2019, 10, 31)
print(oct31_2019)

# to capare both dates
halloween2019 == oct31_2019  # preferred way to compare two dates .. true or false
boolean = halloween2019.year == oct31_2019.year and halloween2019.month == oct31_2019.month and halloween2019.day == oct31_2019.day # a very long way to do this comparison - we dont do it in py

print('-----')

newyears2020 = datetime(2020, 12, 31)  ## checken ob die line so stimmt

halloween2019 < newyears2020
halloween2019 != oct31_2019
halloween2019 != newyears2020
print()
print('-----')

from datetime import timedelta
delta = timedelta(days=11, hours=10, minutes=9, seconds=8)
print(delta.days, delta.seconds, delta.microseconds)  # rechnet dir tage sekunden sec und ms der gesetteten zeit aus
print(delta.total_seconds)  # alle sekunden zusammengerechnet

print()
print('-----')
str(delta)    # gibt string aus mit der zeit






print('------#4  arithmethics with wimedelta-----')
dt = datetime.now()   
thousandDays = timedelta(days=1000)
print(dt)
print(dt + thousandDays)
print(dt - thousandDays)

print('-----')
delta = (dt - newyears2020)   # beides ist type = datetime.datetime, ergebnis ist: datetime.datetime

print(delta.days)


print()
print()

print('------#5  -----')
from dateutil import tz
from datetime import date

## convert between diff. timezones (tz)
usa = "America/Los_Angeles"
usa_tz = tz.gettz(usa)     #get timezone .. gibt tzfile aus

# set tz in daytime
meeting_LA = datetime(2021, 8, 1, hour=13, minute=35, tzinfo=use_tz)
print(meeting_LA)  

# convert with .astimezone():
meeting_LA.astimezone(tz.gettz)

## UNIX Epoch
unix_epoch = datetime.fromtimestamp(0)
print(unix_epoch)  
unix_epoch.astimezone(tz.gettz('UTC'))  # exakte tz




print('------#6  -----')
