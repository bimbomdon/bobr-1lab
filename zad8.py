S = float(input("Введите общую сумму S: "))

vklad1 = float(input("Введите вклад первого участника: "))
vklad2 = float(input("Введите вклад второго участника: "))
vklad3 = float(input("Введите вклад третьего участника: "))

# Считаем общий вклад всех участников
obshiy_vklad = vklad1 + vklad2 + vklad3

# Считаем долю каждого участника от общей суммы
dolya1 = S * vklad1 / obshiy_vklad
dolya2 = S * vklad2 / obshiy_vklad
dolya3 = S * vklad3 / obshiy_vklad

print("Общая сумма:", S)
print("Вклад первого:", vklad1, "получает:", dolya1)
print("Вклад второго:", vklad2, "получает:", dolya2)
print("Вклад третьего:", vklad3, "получает:", dolya3)
print("Общий вклад всех участников:", obshiy_vklad)