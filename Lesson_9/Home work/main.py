tovar = float(input("Введите сумму продукта: "))
skidka = int(input("Введите размер скидки: "))

skilka = tovar * skidka / 100
print(round(skilka, 2))

itog = tovar - skilka
print(round(itog, 2))