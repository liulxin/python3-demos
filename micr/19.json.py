import json

person_dict = {'first': 'Chis', 'last': 'Har'}

person_dict['city'] = 'Seat'

person_json = json.dumps(person_dict)

print(person_json)

# {"first": "Chis", "last": "Har", "city": "Seat"}

language_list = ['CSharp', 'Python', 'JavaScript']
person_dict['languages'] = language_list

person_json = json.dumps(person_dict)

print(person_json)

# {"first": "Chis", "last": "Har", "city": "Seat", "languages": ["CSharp", "Python", "JavaScript"]}
