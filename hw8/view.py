def input_exaple():
    example = input(f'\t\t\t\t\tВведите выражение: ')
    for i in example:
        if i.isdigit() or i == '+' or '-' or '*' or '/': #не пойму почему не отрабатывает условие
            pass
        else:
            print('\t\t\t\t\tВведите корректное выражение')
            return input_exaple()
    return example

def show_example(example: list):
    print(f'\t\t\t\t\tВведено выражение: ', end='')
    print(*example)

def show_result(example: list, old_example: list):
    print(f'\t\t\t\t\tРезультат вычислений: ', end='')
    print(*old_example, end='')
    print(f' = {example[0]}')