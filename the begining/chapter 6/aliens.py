alien_0 = {'color': 'green', 'points': 5, 'speed': 'slow'}
alien_1 = {'color': 'yellow', 'points': 10, 'speed': 'medium'}
alien_2 = {'color': 'red', 'points': 15, 'speed': 'fast'}

aliens = []
for alien in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)



print('Total number of aliens: ' + str(len(aliens)))


for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

print('-'*10)
for alien in aliens[:5]:
    print(alien)


