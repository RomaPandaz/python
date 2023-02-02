example = input('Введите выражение: ')

example = example.replace(' ', '').replace('+', ' + ').replace('-', ' - ').replace('*', ' * ').replace('/', ' / ')

if example.startswith(' - '):
    example = '-' + example[3:]

example = example.split()
orig_example = example.copy()

operation = {'+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y,}

def calculate(operator_1, operator_2):
    i = 0
    while operator_1 in example or operator_2 in example:
        if example[i] in [operator_1, operator_2]:
            example[i-1] = operation.get(example[i])(int(example[i - 1]), int(example[i + 1]))
            example.pop(i)
            example.pop(i)
        else:
            i += 1

while len(example) > 1:
    calculate('*', '/')
    calculate('+', '-')

print(f'{" ".join(orig_example)} = {example[0]}')

# while len(example) > 1:
#     while '*' in example or '/' in example:
#         i = 0
#         while i < len(example):
#             if example[i] == '*':
#                 example[i-1] = int(example[i-1]) * int(example[i+1])
#                 example.pop(i)
#                 example.pop(i)
#             elif example[i] == '/':
#                 example[i-1] = int(example[i-1]) / int(example[i+1])
#                 example.pop(i)
#                 example.pop(i)
#             i += 1

#     while '+' in example or '-' in example:
#         i = 0
#         while i < len(example):
#             if example[i] == '+':
#                 example[i-1] = int(example[i-1]) + int(example[i+1])
#                 example.pop(i)
#                 example.pop(i)
#             elif example[i] == '-':
#                 example[i-1] = int(example[i-1]) - int(example[i+1])
#                 example.pop(i)
#                 example.pop(i)
#             i += 1

# print(example)