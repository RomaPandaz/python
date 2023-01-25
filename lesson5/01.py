string = 'Пиабвтон - полалуй лучшабвий язык в мире'
string = string.split()
new_list = []
for word in string:
    if not 'абв' in word:
        new_list.append(word)
print(' '.join(new_list))
