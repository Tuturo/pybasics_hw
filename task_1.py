# 1
# FizzBuzz

# ввести n
# вывести числа от 1 до n,
# при этом:
# Если число делится на 3, вместо него надо сказать «Fizz».
# Если число делится на 5, вместо него надо сказать «Buzz».
# А если число делится одновременно на 3 и на 5, то надо вместо него сказать «FizzBuzz».

# чтобы преобразовать строку в число, используем функцию int( )

print('Введите число:')

inputNum = int(input())
startNum = 1

for startNum in range(inputNum):
    if startNum % 3 == 0 and startNum % 5 == 0:
        print('FizzBuzz')
        continue
    if startNum % 3 == 0:
        print('Fizz')
        continue
    if startNum % 5 == 0:
        print('Buzz')
        continue
    print(startNum)