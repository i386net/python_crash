users = ['sponge bob', 'patrick', 'sandy', 'admin']
new_users = ['john', 'Patrick', 'michael', 'rose', 'sara']

if len(users) == 0:
    print('We need to find some users!')
else:
    for user in users:
        if user == 'admin':
            print('Hello admin, would you like to see a status report?')
        else:
            print('Hello ' + user.title() + ', thank you for logging in again.')


# checking new_users in users list:

for new_user in new_users:
    if new_user.lower() in users:
        print(new_user.title() + ', you should choose another name!')
    else:
        print('Hello ' + new_user.title())
