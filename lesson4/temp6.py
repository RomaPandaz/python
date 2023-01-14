def create_koef(x):
    print(equation)
    new_koef = []
    nq = equation.replace(' ','').replace('=0','').\
        replace('+',' ').replace('-',' -').split()
    # print(nq)
    for item in nq:
        if item.startswith('x'):
            new_koef.append(1)
        elif item.endswith('-x'):
            new_koef.append(-1)
        else:
            new_koef.append(int(item.split('*x')[0]))
    print(new_koef)

equation = '-61 * x* *2 - x + 25 = 0'
create_koef(equation)