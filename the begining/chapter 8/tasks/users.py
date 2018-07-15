n = int(input('Enter number of users: ')) # number of users

# function for collecting information
def collect_user_info(n):
    users = {}  # dict for users
    details = ['name', 'nickname', 'e-mail']  # list of dict keys
    for num in range(1, n+1):
        bio = {} # dict for user's values
        for detail in details:
            bio[detail] = input('Enter %s for %d user: ' % (detail, num))
        users[num] = bio # add user values as dict to users dict
    return users

# function for printing collected information
def print_info(users_info):
    for id, details in users.items():
        print('User ID: %d' % id)
        for k,v in details.items():
            print("%s: %s" % (k.upper(), v.capitalize()))

# function for printing number of users
def print_tottal_users(users_info):
    print('-'*20)
    print('Total number of users: %d' % len(users.keys()))