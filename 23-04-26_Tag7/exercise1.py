print('-----------TASK 1------------------')
print()

from datetime import datetime           # aus dem modul datatime importiere ich die datatime funtion
current_datetime = datetime.now()       # .now() gibt mir aktuelles datum aus in erstellte variable
print(current_datetime.strftime("%Y"))  # gebe von var mit strftime() die gewünschten teile aus

#   strftime() arguments
#   %Y 	Year e.g. 2012
#   %y 	Year e.g 12
#   %m 	Month
#   %B 	Month full name
#   %b 	Month name abbrevation
#   %d 	day of month
#   %j 	day of year
#   %w 	day of week (starts at 0)
#   %A 	full weekday
#   %a 	weekday name
#   %H 	hours (24h)
#   %I 	hours (12h)
#   %M 	Minute
#   %S 	seconds
#   %p 	'AM'or 'PM'

print()
print()
print('-----------TASK 2------------------')
print()


some_date = datetime(2023, 4, 26)           # ein selbst gewählets datum eingeben
print(some_date.strftime("%w"))             # printed die nummer des wochentags aus, weil mittw.: 3


print()
print()
print('-----------TASK 3------------------')
print()


leap = 2021                                 # ich lege 2021 als jahr fest
if leap % 4 == 0:                           # wenn 2021 durch 4 teilbar ist, % ist der rest 0, dann
    print(leap, "is a leap year")
else:
    print(leap, "is not a leap year")


# oder in etwas umständlicher
some_date = datetime(2021, 12, 31)          # ich setze das datum auf 31.12.21 fest
leap = int(some_date.strftime("%j"))        # ich nehme die zahl des Tages 31.12.21 als int
if leap % 2 == 0:                           # ich schaue ob 265 durch 2 teilbar und rest % == 0 dann
    print(some_date.strftime("%Y"), "is a leap year")
else:
    print(some_date.strftime("%Y"), "is not a leap year")

print()
print()
print('-----------TASK 4------------------')
print()

from datetime import datetime               
date_as_string = "Feb 14 2021 8:30AM"       # jmd gibt das datum als string so ein

dt = datetime.strptime(date_as_string, "%b %d %Y %H:%M%p")  # mit strptime -> string zu datum
print(dt)

# hier ist wichtig die argumente korrekt auszugeben wie oben
# strptime() argumente: dirhr oben
