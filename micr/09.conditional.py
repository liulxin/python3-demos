# price = input('how much did you pay? ')
# price = float(price)

# if price >= 1.00:
#   tax = .07
# else:
#   tax = 0
# print('Tax rate is: ' + str(tax))



country = input('enter the name of your home country ')
# if country.lower() == 'canada':
#   print('so you must like hockey')
# else:
#   print('you are not from canada')


province = input('what province do you live in? ')
tax = 0

# if province == 'alberta':
#   tax = 0.05
# if province == 'nunavut':
#   tax = 0.07
# if province == 'ontario':
#   tax = 0.13

# if province == 'alberta':
#   tax = 0.05
# elif province == 'nunavut':
#   tax = 0.07
# elif province == 'ontario':
#   tax = 0.13
# else:
#   tax = 0.1

# if province == 'alberta' or province == 'nunavut':
#   tax = 0.05
# elif province == 'ontario':
#   tax = 0.13
# else:
#   tax = 0.1

if country.lower() == 'canada':
  if province in ('alberta', 'nunavut'):
    tax = 0.05
  elif province == 'ontario':
    tax = 0.13
  else:
    tax = 0.1
else:
  tax = 0

print(tax)