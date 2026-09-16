import math

a = float(input("Введите первый катет: "))
b = float(input("Введите второй катет: "))

c = math.sqrt(a ** 2 + b ** 2)

s = (a * b) / 2

print("Первый катет:", a)
print("Второй катет:", b)
print("Гипотенуза:", c)
print("Площадь треугольника:", s)