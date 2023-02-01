import model
import controller

commands = ['Открыть файл',
    'Сохранить файл',
    'Показать все контакты',
    'Создать контакт',
    'Удалить контакт',
    'Изменить контакт',
    'Найти контакт',
    'Выход из программы']

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

def show_contacts(phone_list: list):
    if len(phone_list) < 1:
        print(f'\t\t\t\t\tТелефонная книга пуста или не октрыта')
        return controller.start()
    else:
        for i, contact in enumerate(phone_list, 1):
            print(f'\t{i}. {contact[0]:20} {contact[1]:13}')

def input_error():
    print(f'\t\t\t\t\tОшибка ввода. Введите корреткный пункт меню')

def create_new_contact():
    name = input(f'\t\t\t\t\tВведите ФИО: ')
    phone = input(f'\t\t\t\t\tВведите номер телефона: ')
    return name, phone

def find_contact():
    find = input(f'\t\t\t\t\tВведите искомый эллемент: ')
    return find

def del_contact(pb):
    delete_num = int(input(f'\t\t\t\t\tКакой элемент удалить? '))
    return delete_num

def edit_contact():
    edit_num = int(input(f'\t\t\t\t\tКакой элемент изменить? '))
    return edit_num

def message_opened():
    print(f'\t\t\t\t\tФайл открыт')