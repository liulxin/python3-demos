first_name = input('enter your first name: ')
last_name = input('enter your last name: ')

def initial_name(name, force_uppercase = True):
  if force_uppercase:
    initial = name[0:1].upper()
  else:
    initial = name[0:1]
  return initial

print(f'Your initials are: {initial_name(name = first_name, force_uppercase = False)} {initial_name(name = last_name)}')