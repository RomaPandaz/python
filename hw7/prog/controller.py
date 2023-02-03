import view
import model_r
import model_w

def start():
    pb = model_r.open_file()
    choice = ''
    while choice !=3:
        choice = view.main_menu()

        match choice:
            case 1:
                new = view.create_new_contact()
                model_w.add_new_contact(new, pb)
                model_w.save_file(pb)
            case 2:
                model_r.show_contacts(pb)
            case 3:
                pass
            case _:
                view.input_error()