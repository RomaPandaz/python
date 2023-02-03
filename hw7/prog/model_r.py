import controller
import model_r
import model_w

phone_book =[]
path = 'python\hw7\prog\phone_book.txt'

def open_file():
    global phone_book
    global path
    with open (path, 'r', encoding='UTF-8') as data:
        file = data.readlines()
        phone_book = [x.strip().split(';') for x in file]
    return phone_book

def show_contacts(phone_list: list):
    if len(phone_list) < 1:
        print(f'\t\t\t\t\tТелефонная книга пуста')
        return controller.start()
    else:
        for i, contact in enumerate(phone_list, 1):
            print(f'\t{i}. {contact[0]:10} {contact[1]:10} {contact[2]:10} {contact[3]:20} {contact[4]:10}')
