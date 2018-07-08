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


# 5-10 checking new_users in users list:

for new_user in new_users:
    if new_user.lower() in users:
        print(new_user.title() + ', you should choose another name!')
    else:
        print('Hello ' + new_user.title())

#5-11

for num in list(range(1,10)):
    if num == 1:
        print(str(num) + 'st')
    elif num == 2:
        print(str(num) + 'nd')
    elif num == 3:
        print(str(num) + 'rd')
    else:
        print(str(num) + 'th')
