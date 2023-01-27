# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

my_string = 'AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE11'  #сжатие
def rle_in(my_string: str):
    final_string = ''
    count = 1
    my_string = my_string + '_'
    for i in range(len(my_string)-1):
        if my_string[i] == my_string[i+1]:
            count = count + 1
        else:
            final_string = final_string + my_string[i] + str(count)
            count = 1
    file = open('rle_in.txt', 'w+')
    file.write(final_string)
    file.close()
    return final_string


def rle_out(file_name):     #восстановление
    file = open(file_name, 'r')
    my_string = file.read()
    file.close()
    rle_out = ''
    for i in range(len(my_string)):
        if my_string[i].isdigit():
            rle_out = rle_out + my_string[i-1] * int(my_string[i])
    file = open('rle_out.txt', 'w+')
    file.write(rle_out)
    file.close()
    return rle_out

print(rle_in(my_string))    #сжаие

print(rle_out('rle_in.txt'))    #восстановление

