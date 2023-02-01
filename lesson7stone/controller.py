# 1. Открыть файл
# 2. Сохранить файл
# 3. Показать все контакты
# 4. Создать контакт
# 5. Удалить контакт
# 6. Изменить контакт
# 7. Найти контакт
# 8. Выход из программы

import view
import model



def start():
    choice = ''
    while choice != 8:
        choice = view.main_menu()

        match choice:
            case 1:
                model.open_file()
                view.message_opened()
            case 2:
                model.save_file()
            case 3:
                pb = model.get_phone_book()
                view.show_contacts(pb)
            case 4:
                new_contact = (view.create_new_contact())
                model.add_new_contact(new_contact)
            case 5:
                pb = model.get_phone_book()
                view.show_contacts(pb)
                del_num = (view.del_contact(pb))
                model.delete(pb, del_num)
            case 6:
                pb = model.get_phone_book()
                view.show_contacts(pb)
                edit_num = (view.edit_contact())
                new_contact = (view.create_new_contact())
                model.edite(edit_num, new_contact)
            case 7:
                find = view.find_contact()
                result = model.search_contact(find)
                view.show_contacts(result)
            case 8:
                pass
            case _:
                view.input_error()