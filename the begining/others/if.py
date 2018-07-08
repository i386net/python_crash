phone = 'iphone'
print(phone.title() == 'iPhone')
print(phone == 'iphone')
phone = list(phone)
phone[1] = phone[1].title()
print(phone)
phone = ''.join(phone)
print(phone == 'iPhone' or phone == 'iphone')
print(phone == 'iPhone' and phone == 'iphone')

nums = range(10)
if 1 in nums:
    print('1 is in numbers list')
if 20 not in nums:
    print('20 is not is list')
if 5 in nums and 10 not in nums:
    print('Nooooo!')
    
    
alien_color = 'red'
if alien_color == 'green':
    print("You've got 5 scores!")
elif alien_color == 'yellow':
    print("You've got 10 scores!")
else:
    print("You've got 15 scores!")
    
age = int(input())

if age < 2:
    print('младенец')
elif  age <4:
    print('малыш')
elif age < 13:
    print('ребёнок')
elif age < 20:
    print('подросток')
elif age < 65:
    print('взрослый')
else:
    print('пожилой')
