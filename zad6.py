# int() — целое число, float() — число с точкой
n = int(input("Введите количество товаров: "))
p = float(input("Введите цену одного товара: "))
s = float(input("Введите размер скидки в процентах: "))

# Считаем стоимость без скидки
summa_bez_skidki = n * p

# Считаем саму скидку 
razmer_skidki = summa_bez_skidki * s / 100

# Итоговая сумма к оплате
itog = summa_bez_skidki - razmer_skidki

# Выводим результат с пояснениями
print("Количество товаров:", n)
print("Цена одного товара:", p)
print("Скидка:", s, "%")
print("Стоимость без скидки:", summa_bez_skidki)
print("Размер скидки:", razmer_skidki)
print("Итоговая стоимость со скидкой:", itog)