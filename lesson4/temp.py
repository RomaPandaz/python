my_string = 'Питон самый лучший в мире язык'

my_string1 = '\tПитон самый лучший в мире язык\n'

my_string2 = 'Питон самый лучший в мире язык'

my_list = ['21', '23', '543', '43', 'gt', '654fgdf']
add = '-'

new_string = my_string.split()

new_string1 = my_string.replace('и', '$')

new_string2 = my_string1.strip()

print(my_string)

print(new_string)

print(new_string1)

print(new_string2)

if my_string.startswith('Пит'):
    print('Да, все верно')

if my_string.endswith('зык'):
    print('Да, все верно')

if my_string2.lower().startswith('пит'): #upper()
    print('Да, все верно')

print(add.join(my_list))