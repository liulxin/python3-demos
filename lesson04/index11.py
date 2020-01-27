import re

lang = 'PhthonC#javaphp'

res = re.sub('C#', 'Go', lang)

lang1 = 'PhthonC#javaphp'

lang2 = lang1.replace('C#', 'Go')

print(res)  # PhthonGojavaphp

print(lang2)  # PhthonGojavaphp

def convert(value):
    matched = value.group()
    print(matched)
    return '--' + matched + '!!'

res2 = re.sub('C#', convert, lang)

print(res2) # Phthon--C#!!javaphp