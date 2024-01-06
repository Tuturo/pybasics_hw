# 2
# Определить корни квадратного уравнения
# Коэффициенты ввести с клавиатуры

import math

print("Квадратное уравнение рассчитывается по формуле: 'ax^2 + bx + c = 0'")
print("Введите значения:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
 
discr = b ** 2 - 4 * a * c
print("Дискриминант D = %.2f" % discr)
 
if discr > 0:
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
elif discr == 0:
    x = -b / (2 * a)
    print("x = %.2f" % x)
else:
    print("Корней нет")