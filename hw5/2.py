# Создайте программу для игры в ""Крестики-нолики"".

# tkinter



# print(' 1 | 2 | 3 ')
# print('-----------')
# print(' 4 | 5 | 6 ')
# print('-----------')
# print(' 7 | 8 | 9 ')

matrix = [[1,2,3],[4,5,6],[7,8,9]]
# print(matrix[0])
# print(matrix[1])
# print(matrix[2])

x = 5

for row in matrix:
    for elem in row:
        if elem == x:
            matrix[elem,row] = 9

print(matrix)