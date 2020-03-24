gpa = float(input('what was your grade point average? '))
lowest_grade = float(input('what was your lowest grade? '))

# if gpa >= 0.85:
#   if lowest_grade >= 0.70:
#     print('you made the honour roll')


if gpa >= 0.85 and lowest_grade >= 0.7:
  honour_roll = True
else:
  honour_roll = False

if honour_roll:
  print('you made the honour roll')