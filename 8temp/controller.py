import view
import add_students
import add_perfomance

def button():
    journal = {}
    lst_stud = []
    lst_less = []
    flag = True
    while flag == True:
        a = view.viewer()
        if a == 1:
            student = add_students.st_name()
            if student not in lst_stud:
                journal[student] = {}
                lst_stud.append(student)
                if lst_less:
                    for less in lst_less:
                        journal[student][less] = []
        elif a == 2:
            less = add_students.st_less()
            if less not in lst_less:
                lst_less.append(less)
                for name in lst_stud:
                    journal[name][less] = []
        elif a == 3:
            name, less, perf = add_perfomance.add_perf()
            journal[name][less].append(perf)
        elif a == 4:
            print(journal)
        elif a == 5:
            name = add_students.st_name()
            print(f'Оценки ученика {name}: {journal[name]}')
        elif a == 6:
            flag = False

button()