my_string = '12 574 839 756 3894'
print(my_string)

print('--------------')

my_list = list(map(int, my_string.split()))
print(my_list)

print('--------------')

my_list = list(filter(lambda x: '4' in x, my_string.split())) #фильтр из строки с !символом! 4
print(my_list)

print('--------------')

my_list = list(filter(lambda x: x%2 == 0, list(map(int, my_string.split()))))# фильтр всех четных с переводом в int
print(my_list)

print('--------------')

my_list = my_string.split()
print(my_list)

for i in range(len(my_list)):
    print(my_list[i])
    print(i)

for i, item in enumerate(my_list):
    print(i, item)