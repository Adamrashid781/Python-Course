
from datetime import datetime, timedelta
from pytz import timezone
import pytz
import os 



format = "%H:%M"

nyc = datetime.now(timezone('EST'))
london = datetime.now(timezone('GMT'))
portland = datetime.now(timezone('US/Pacific'))

# nyc = datetime( 2020, 12, 10,  tzinfo=ZoneInfo("America/Los_Angeles"))
print('The time in NYC is: ' + nyc.strftime(format))
print('The time in London is: ' + london.strftime(format))
print('The time in Portland is: ' + portland.strftime(format))

if str(nyc.hour) >= '09:00' and str(nyc.hour) <= '17:00': 
    # print('hello1')
    # if str(nyc.hour) >= '17:00':
    print("The New York City Branch is currently open")


if str(london.hour) >= '09:00' and str(london.hour) <= '17:00': 
    # print('hello2')
    # if str(london.hour) >= '17:00':
    print("The London Branch is currently open")

if str(portland.hour) >= '09:00' and str(portland.hour) <= '17:00': 
    # print('hello3')
    # if str(portland.hour) <= '17:00':
    print("The Portland Branch is currently open")

# zones = pytz.all_timezones
# print(zones)


