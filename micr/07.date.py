from datetime import datetime, timedelta

birthday = input('When is your birthday (dd/mm/yyyy) ?')
birthday_date = datetime.strptime(birthday, '%d/%m/%Y')

print('Birthday: ' + str(birthday_date))