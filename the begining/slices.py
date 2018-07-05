players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(*players)
print('The 3 first elements of this list are: ', *players[:3])
print('the 3 elements from the middle of the list are: ', players[1:4])
print('the last 3 elements are: ', players[-3:])


new_players = players[:]
print('new players list:', new_players)
new_players.append('jack')
print('really new players list:', new_players)
l = len(new_players)
if l%2 != 0:
	print(new_players[l//2-1:l//2+2])
else:
	
	print(new_players[l//2-1:l//2+1])
