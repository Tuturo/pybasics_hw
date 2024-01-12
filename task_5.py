#5
# дан список. Найти самую продолжительную возрастающую последовательность его элементов
# (в упрощенном варианте - выдать только длину этой последовательности)

l= [1,0,5,3,2,3,4,5,6,12,1,2,3,5,6,3,12,18,20]

def get_greatest_sequence(array):

    greatest_seq = []
    current_seq = []
    num = 0

    for i in range(len(array)):
        if array[i] >= num:
            current_seq.append(array[i])
            num = array[i]
        else:
            if len(current_seq) > len(greatest_seq):
                greatest_seq = current_seq
                current_seq = []
                num = array[i]
            else:
                current_seq = []
                current_seq.append(array[i])
                num = array[i]

    print(f'Самая продолжительная последовательность – {len(greatest_seq)} элементов')
    print('Состоит из элементов:')
    print(greatest_seq)
            

get_greatest_sequence(l)