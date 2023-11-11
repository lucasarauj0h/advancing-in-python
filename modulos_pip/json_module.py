import json

person = '{"name":"Lucas", "language":["Python","JavaScript"]}'
person_dict = json.loads(person)
print(person_dict)
print('att')