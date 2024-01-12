# 7
# ввести строку
# вывести ее "лесенкой"
# п
#  р
#   и
#    в
#     е
#      т


print('Введите строку:')
current_string = input()
indent = ''


for i in range(len(current_string)):
    print(indent + current_string[i])
    indent += ' '

print('Строка лесенкой!')