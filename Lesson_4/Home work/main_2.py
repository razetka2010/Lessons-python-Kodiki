import random
from tkinter import *

root = Tk()
root.geometry("350x200")
root.title("Рандомайзер никнеймов")

ajectives = ["Весёлый", "Грозный", "Ленивый", "Крутой", "Безграничный"]
colors = ['Чёрный', 'Белый', 'Красный', 'Жёлтый', 'Голубой']
animals = ['Кот', 'Собака', 'Волк', 'Ёжик', 'Лиса', 'Медведь']

def random_nick():
    adjective = random.choice(ajectives)
    color = random.choice(colors)
    animal = random.choice(animals)
    result.config(text=f"Результат: {adjective}{color}{animal}")

label = Label(root, text="Сгенерировать никнейм")
label.pack()

button = Button(root, text="Сгенерировать", command= random_nick)
button.pack()

result = Label(root, text=" ")
result.pack()

root.mainloop()
