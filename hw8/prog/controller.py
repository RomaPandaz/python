import view
import model


def start():
# pb = model_r.open_file()
    choice = ''
    while choice !=6:
        choice = view.main_menu()

        match choice:
            case 1:
                view.show_person()
            case 2:
                new_person = view.input_person()
                study_list = view.person_lst()
                model.add_person(new_person,study_list)
            case 3:
                new_subjects = view.input_subjects()
                subject_list = view.subjects_lst()
                print(subject_list)
                model.add_subjects(new_subjects,subject_list)
                print(subject_list)
            case 4:
                pass
            case 5:
                pass
            case 6:
                pass
            case _:
                view.input_error()