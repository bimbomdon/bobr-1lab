import math

R = float(input("Введите радиус основания R: "))
H = float(input("Введите высоту H: "))

# Объём цилиндра
V = math.pi * R ** 2 * H

# Площадь полной поверхности
S = 2 * math.pi * R ** 2 + 2 * math.pi * R * H

print("Радиус R:", R)
print("Высота H:", H)
print("Объём цилиндра:", V)
print("Площадь поверхности цилиндра:", S)