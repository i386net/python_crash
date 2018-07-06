users = ['sponge bob', 'patrick', 'sandy', 'admin']


if len(users) == 0:
    print('We need to find some users!')
else:
    for user in users:
        if user == 'admin':
            print('Hello admin, would you like to see a status report?')
        else:
            print('Hello ' + user.title() + ', thank you for logging in again.')

