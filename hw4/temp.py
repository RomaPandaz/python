import random

def get_random_params(num=2, min_value=0, max_value=100):
    params_list = []
    params_list.append(random.randint(min_value + 1, max_value))
    if num > 0:
        for _ in range (1, num + 1):
            params_list.append(random.randint(min_value, max_value))
    return params_list

def generate_equation(params_list):
    equation_power = len(params_list)
    result = ''
    for i in params_list:
        equation_power -= 1
        if i != 0:
            result += f'{i}'
            if equation_power > 0:
                result += f'*x^{equation_power} + '
    result += ' = 0'
    return result


num = 2
params_list = get_random_params(num)
print (params_list)
equation_string = generate_equation(params_list)
print(equation_string)
file_obj = open('task4.txt', 'w')
file_obj.write(equation_string)
file_obj.close()