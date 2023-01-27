def print_matrix(matrix: list): 
    for row in matrix: 
        print(*row) 
 
def x_in_matrix(input_digit: int, matrix: list): 
    row = (input_digit-1) // len(matrix[0]) 
    col = (input_digit-1) % len(matrix[row]) 
    matrix[row][col] = ' X ' 
    print_matrix(my_matrix) 
    print('----------') 
    return matrix 
 
def o_in_matrix(input_digit: int, matrix: list): 
    row = (input_digit-1) // len(matrix[0]) 
    col = (input_digit-1) % len(matrix[row]) 
    matrix[row][col] = ' O ' 
    print_matrix(my_matrix) 
    print('----------') 
    return matrix 
 
my_matrix = [ 
    [' 1 ', ' 2 ', ' 3 '], 
    [' 4 ', ' 5 ', ' 6 '], 
    [' 7 ', ' 8 ', ' 9 '] 
] 
 
print_matrix(my_matrix) 
 
# while my_matrix[2][0] != ' X ' or my_matrix[1][1] != ' X ' or my_matrix[0][2] != ' X ' and \ 
#     my_matrix[0][0] != ' X ' or my_matrix[1][1] != ' X ' or my_matrix[2][2] != ' X ' and \ 
#     my_matrix[0][0] != ' O ' or my_matrix[1][1] != ' O ' or my_matrix[2][2] != ' O ' and \ 
#     my_matrix[0][0] != ' O ' or my_matrix[1][1] != ' O ' or my_matrix[2][2] != ' O ' and \ 
#     my_matrix[0] != [' X ', ' X ', ' X '] and my_matrix[1] != [' X ', ' X ', ' X '] and my_matrix[2] != [' X ', ' X ', ' X '] and \ 
#     my_matrix[0] != [' O ', ' O ', ' O '] and my_matrix[1] != [' O ', ' O ', ' O '] and my_matrix[2] != [' O ', ' O ', ' O ']: 
while True: 
    x_in_matrix(int(input('Где поставим X? ')), my_matrix) 
    o_in_matrix(int(input('Где поставим O? ')), my_matrix) 
 
 
    # print('Игра окончена!')