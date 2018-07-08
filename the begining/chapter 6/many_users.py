users = {
    'aeinstein' : {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton'
    },
    'mcurie': {
        'first': 'matie',
        'last': 'curie',
        'location': 'paris'
    }
}

for username, user_info in users.items():
    print(username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    print("\t " + full_name.title())
    print("\t " + location.title())