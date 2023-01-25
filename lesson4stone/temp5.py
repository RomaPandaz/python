
def conv(x):
    temp = string.split('x')
    print(temp) 
    temp2 = []
    for i in range(len(temp)):
        temp2.append(temp[i].replace('**2','').replace(' ','').replace('*','').replace('=0','').replace('= 0','').replace('+',''))
    return temp2

string = '10*x**2 + 20*x + 30 =0'
a = conv(string)
print(a)

for i in range(len(a)):
    a[i] = int(a[i])
print(a)