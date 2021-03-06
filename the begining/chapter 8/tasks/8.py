# 8-1

def display_message():
    print('Python is great!')


for i in range(5):
    display_message()


# 8-2

def favorite_book(title):
    print("One of my favorite books is " + title.title())


# favorite_book(input('Type in your favorite book '))

# 8-3

def make_shirt(size='L', text='I love Python'):
    print("T-shirt size: " + size)
    print("T-shirt print: " + text.upper())


#make_shirt()

# 8-4

#make_shirt('S', 'I love C++')


# 8-5

def describe_city(city, country='USA'):
    if len(country) <= 3:
        print(city.title() + ' is in ' + country.upper())
    else:
        print(city.title() + ' is in ' + country.title())


cities = {
    'New York': ' ',
    'Moscow': 'Russia',
    'London': 'GB'
}

for city, country in cities.items():
    if cities[city] == ' ':
        country = 'USA'
    describe_city(city, country)

#8-6

def city_country(city, country):
    return '%s, %s' % (city, country)

cities = ['London', 'Paris', 'NY']
countries = ['GB', 'France', 'USA']

for k, v in dict(zip(cities, countries)).items():
    cc = city_country(k, v)
    print(cc)

#8-7
def album_make(album, artist, tracks=0):
    if tracks:
        return {'album': album.title(), 'artist': artist.title(), 'tracks': tracks}
    else:
        return {'album': album, 'artist': artist}

#a1 = album_make('AAAA', 'BBB', 10)
#b1 = album_make('NNN')
#c1 = album_make()
#print('%s\n%s\n%s ' % (a1, b1, c1))

# 8-8
mus_list = []
while True:
    album = input('Album: ')
    if album == 'q':
        break
    artist = input('Artist: ')
    #tracks = input('Tracks: ')
    music_collection = album_make(album, artist)
    mus_list.append(music_collection)
    if input('Next: ').lower() == 'n':
        break
#print(*mus_list)

# 8-9
def show_magicians(names):
    for name in names:
        print(name.title())

magicians = ['alice', 'mike', 'ed']

#show_magicians(magicians)

# 8-10
def make_great(magicians):
    great_magicians=[]
    while magicians:
        magician = magicians.pop() + ' the great!'
        great_magicians.append(magician)

    for great_magician in great_magicians:
        magicians.append(great_magician)

    return magicians

#make_great(magicians)
#show_magicians(magicians)

# 8-11

great_mags = make_great(magicians[:])
#show_magicians(magicians)
#show_magicians(great_mags)

# 8-12

def sandwich(*fillings):
    for f in fillings:
        print('• %s' % f.title())

s_list = ['apple', 'ham', 'carry']
#sandwich('apple', 'ham', 'carry')
sandwich(*s_list)

# 8-13

def build_profile(first, last, **user_info):
    '''buid dict with user info'''
    profile = {}
    profile['first_ name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('bill', 'lubanovic',
                             occupation='writer', book='introducing python', year=2017)
print(user_profile)

# 8-14 (cars function)

def make_car(maker, model, **car_details):
    car = {
        'maker':maker,
        'model': model
    }
    for k, v in car_details.items():
        car[k] = v
    return car

car = make_car('subaru', 'forester', color='red')
print(car)
