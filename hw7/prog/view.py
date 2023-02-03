import controller
commands = ['Добавить контакт', 'Показать контакты', 'Выход из программы']

def main_menu():
    print('Главное меню:')
    for i, item in enumerate(commands, 1):
        print(f'\t{i}. {item}')
    choice = input(f'\t\t\t\t\tВыберите пункт меню: ')
    if choice.isdigit():
        pass
    else:
        print(f'\t\t\t\t\tВыберите корректный пункт меню')
        return main_menu()
    print('')
    return int(choice)

def input_error():
    print(f'\t\t\t\t\tОшибка ввода. Введите корреткный пункт меню')

def create_new_contact():
    id = input(f'\t\t\t\t\tВведите ID: ')
    name1 = input(f'\t\t\t\t\tВведите Имя: ')
    name2 = input(f'\t\t\t\t\tВведите Фамилию: ')
    phone = input(f'\t\t\t\t\tВведите номер телефона: ')
    als = input(f'\t\t\t\t\tВведите орисание: ')
    return id, name1, name2, phone, als