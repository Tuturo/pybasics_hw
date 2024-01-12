# 4

# Найти сумму положительных элементов в матрице 4 на 4, представленной вложенными списками

l = [[1, 2, 3, -1],
     [5, 4, 4, 6],
     [1, -3, 2, -3]]


def get_sum_elements(matrix):
    ''' Решение через len() '''

    sum_elem = 0

    for i in range(len(matrix)):

        for j in range(len(matrix[i])):

            if matrix[i][j] > 0:
                sum_elem += matrix[i][j]

    print(sum_elem)


def get_sum_elements_two(matrix):
    ''' Решение через enumerate '''

    sum_elem = 0

    for i, data in enumerate(matrix):

        for j, num in enumerate(data):

            if num > 0:
                sum_elem += num

    print(sum_elem)

get_sum_elements(l)
get_sum_elements_two(l)