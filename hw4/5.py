# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

equation = '-83*x^5 + 43*x^4 + 6*x^3 - 39*x^2 + 28*x + 78 = 0'
dict = {}
equation = equation.replace(' = 0', '')
equation = equation.replace('-', '+ -')
equation = equation.replace('- ', '-')


for i in equation.split(' + '):
    list = i.split("x")
    if len(list) == 1:
        dict.update({"0": list[0].replace('*', '')})
    else:
        if list[1] == '':
            dict.update({"1": list[0].replace('*', '')})
        else:
            dict.update(({list[1].replace('^', ''): list[0].replace('*', '')}))
print(dict)