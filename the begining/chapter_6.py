# 6-1
batman = {
    'name': 'bruce',
    'surname': 'wayne',
    'age': '79',
    'city': 'gotham city'
}

for k, v in batman.items():
    print(k.upper() + ': ' + v.title())

# 6-2

favorite_numbers = {
    'jesus': 3,
    'satan': 666,
    'pifagor': 3.14,
    'duke nukem': 1000000
}

for k, v in favorite_numbers.items():
    print(k.upper(), v)

# 6-3

python_themes = {
    'string': 'упорядоченная неизменяемая последовательность',
    'list': 'упорядоченная изменяемая последовательность',
    'dictionary': 'неупорядоченная последовательность, содержащая пары ключ - значение',
    'comments': 'описывают подход к решаемой задаче'
}

for p in python_themes.items():
    print(p[0].capitalize() + ':')
    print('\t\t' + p[1].capitalize())

# sorting dictionaty keys

test_dict = {
    'a': 1, 'b': 2, 'd': 3, 'c': 4
}

for key in test_dict.keys():
    print(key)
# print sorted keys
for key in sorted(test_dict.keys()):
    print(key)
# print sorted keys
print(*sorted(test_dict.keys()))

# 6-4

