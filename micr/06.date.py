from datetime import datetime, timedelta

today = datetime.now()

print('Today is: ' + str(today))

one_day = timedelta(days=1)
yesterday = today - one_day
print('Yesterday is: ' + str(yesterday))

one_week = timedelta(weeks=1)
last_week = today - one_week
print('Last week is: ' + str(last_week))

print('Day: ' + str(today.day))
print('Month: ' + str(today.month))
print('Year: ' + str(today.year))
print('Hour: ' + str(today.hour))
print('Minute: ' + str(today.minute))
print('Second: ' + str(today.second))