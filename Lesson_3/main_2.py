import random

colors = ['Чёрный', 'Белый', 'Красный', 'Жёлтый', 'Голубой']
print(colors)

color = random.choice(colors) #Вывод любого цвета из colors
print(color)

color2 = random.choice(color) #Вывод любой буквы из color
print(color2)