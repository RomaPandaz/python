import controller
import model_r

phone_book =[]
path = 'python\hw7\prog\phone_book.txt'

def add_new_contact(new_contact: list, pb: list):
    pb.append(new_contact)

def save_file(pb: list):
    pb_str = []
    for contact in pb:
        pb_str.append(';'.join(contact))
    with open(path, 'w', encoding='UTF-8') as data:
        data.write('\n'.join(pb_str))