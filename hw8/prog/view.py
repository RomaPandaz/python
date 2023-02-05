


person_list = ['Бобров Артур', 'Александрова Алиса']#, 'Рубцов Данила',\
        # 'Галкина Виктория','Дмитриев Демьян', 'Ефремова Кристина',\
        # 'Ушаков Николай', 'Дмитриева Мила', 'Афанасьев Григорий']

subjects_list = ['Обществознание', 'Алгебра']#, 'Информатика', 'Физика', 'Геометрия', 'Черчение']

menu_list = ['Все ученики', 'Добавить ученика','Добавить предмет',\
            'Добавление оценки по предмету', 'Лист оценок ученика', 'Выход из программы']

temp_dickt = {}
for i in subjects_list: #словарь предмет: оценка
    temp_dickt[i] = []

temp_dickt2 ={}
for i in person_list: # словарь ученик: предмет: оценка
    temp_dickt2[i] = temp_dickt

print(temp_dickt2)
for i in temp_dickt2: # добавление нового предмета
    temp_dickt['НОВЫЙ ПРЕДМЕТ'] = []

# temp_dickt2[2]

temp_dickt2['Александрова Алиса'] = temp_dickt2.get('Александрова Алиса',[]) + ['sss']






def main_menu():
    print(f'\t\t\t\t\tГлавное меню:')
    for i, item in enumerate(menu_list, 1):
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

def show_person():
    digit = 1
    if len(person_list) < 1:
        print('Список учеников пуст =(')
    else:
        for i in range(len(person_list)):
            print(f'{digit}.{person_list[i]}')
            digit = digit + 1
    print()

def input_person():
    new_person = input('Введите Имя и Фамилию: ')
    a = input(f'Ученика зовут {new_person}. Верно? 1 - подтвердить, 2 - повторить ввод: ')
    while a != '1':
        return input_person()
    return(new_person)

def input_subjects():
    new_subjects = input('Введите наименование предмета: ')
    a = input(f'Новая дисциплина - {new_subjects}. Верно? 1 - подтвердить, 2 - повторить ввод: ')
    while a != '1':
        return input_subjects()
    return(new_subjects)

def person_lst():
    return person_list

def subjects_lst():
    return subjects_list