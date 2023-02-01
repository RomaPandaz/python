# 1. Открыть файл
# 2. Сохранить файл
# 3. Показать все контакты
# 4. Создать контакт
# 5. Удалить контакт
# 6. Изменить контакт
# 7. Найти контакт
# 8. Выход из программы

phone_book =[]
path = 'python\lesson7stone\phone_book.txt'

def open_file():
    global phone_book
    global path
    with open (path, 'r', encoding='UTF-8') as data:
        file = data.readlines()
        phone_book = [x.strip().split(';') for x in file]

def get_phone_book():
    global phone_book
    return phone_book

def add_new_contact(new_contact):
    global phone_book
    phone_book.append(new_contact)

def search_contact(find: str):
    global phone_book
    result = []
    for contact in phone_book:
        for field in contact:
            if find in field:
                result.append(contact)
                break
    return result

def save_file():
    global phone_book
    global path
    pb_str = []
    for contact in phone_book:
        pb_str.append(';'.join(contact))
    with open(path, 'w', encoding='UTF-8') as data:
        data.write('\n'.join(pb_str))

def delete(phone_book: list, num: int):
    phone_book.pop(num-1)

def edite(num, my_list):
    global phone_book
    phone_book.insert(num, my_list)
