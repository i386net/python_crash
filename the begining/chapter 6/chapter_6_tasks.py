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

# 6-6

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

users_list = ['michael', 'Jen', 'john', 'edward', 'ken', 'david']
for user in users_list:
    if user.lower() in favorite_languages.keys():
        print('Thank you, ' + user.title() + ', for your participation in this poll!')
    else:
        print(user.title() + ", what's your favorite programming language?")


# 6-7

batman = {
    'name': 'bruce',
    'surname': 'wayne',
    'age': '79',
    'city': 'gotham city'
}

superman = {
    'name': 'clark',
    'surname': 'kent',
    'age': '80',
    'city': 'metropolice'
}

darkseid = {
    'name': 'uxas',
    'surname': '',
    'age': '245.000 ',
    'city': 'apokolips'
}

dc_chars = [batman, superman, darkseid]
print('-'*20)
for character in dc_chars:
    full_name = character['name'] + ' ' + character['surname']
    print('Name: ' + full_name.title())
    print('Age: ' + character['age'].title() )
    print('Location: ' + character['city'].title())
    print('-'*20)


# 6-8
pets = []
pet = {
    'animal type': 'dog',
    'name': 'ball',
    'owner': 'bart',
    'weight': 43,
    'eats': 'bones',
}
pets.append(pet)
pet = {
    'animal type': 'cat',
    'name': 'furfur',
    'owner': 'candy',
    'weight': 10,
    'eats': 'fish',
}
pets.append(pet)

pet = {
    'animal type': 'bird',
    'name': 'mr. crow',
    'owner': 'john',
    'weight': 1.5,
    'eats': 'bugs',
}
pets.append(pet)

for pet in pets:
    message = pet['owner'].title() + " own's '" + pet['name'].title() + "' and this is a " + pet['animal type'] \
              + ". He's " + str(pet['weight']) + ' kgs and like to eat ' + pet['eats'] + "."
    print(message)
    if pet['animal type'] == 'dog':
       print('Bark-Bark!!! 🐶')
    elif pet['animal type'] == 'cat':
        print('Meow-Meow!!! 🐱')
    else:
        print('Tweet-Tweet!!! 🐦')

# 6-9

fav_places = {
    'john':['m1', 'm2', 'm3'],
    'mike': ['p1', 'p2', 'p3'],
    'duke': ['l1', 'l2', 'l3']
}

for name, places in fav_places.items():
    print(name.title() + "'s favourite places are: ")
    for place in places:
        print("• " + place.title())


# 6-10

favorite_numbers = {
    'jesus': [3, 33, 7],
    'satan': [666, 56, 5],
    'pifagor': [3.14, 4, 9.8],
    'duke nukem': [1000000, 4324, 5656]
}

for name, numbers in favorite_numbers.items():
    print(name.title() + ':')
    print(*numbers)

# 6-11
cities = {
    'santiago': {
        'country': 'chile',
        'population': 6158080,
        'nearby mountains': 'andes',
        },
    'talkeetna': {
        'country': 'alaska',
        'population': 876,
        'nearby mountains': 'alaska range',
        },
    'kathmandu': {
        'country': 'nepal',
        'population': 1003285,
        'nearby mountains': 'himilaya',
        }
    }
for city, city_info in cities.items():
    city_name = city.title()
    city_location = city_info['country'].title()
    city_population = str(city_info['population'])
    mountain = city_info['nearby mountains'].title()

    print(city_name + ': \n\t• ' + city_location + '\n\t• ' + city_population + '\n\t• ' + mountain)