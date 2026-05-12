from tkinter import *
import random


root = Tk()
root.geometry("300x200")
root.title("Животные")

animals = ['Кот', 'Собака', 'Волк', 'Ёжик', 'Лиса', 'Медведь']

def random_animals():
    amimal = random.choice(animals)
    result_animal.config(text=f"Животное дня: {amimal}")

label = Label(root, text="Животное дня.")
label.pack()

button = Button(root, text="Показать.",  command=random_animals)
button.pack()

result_animal = Label(root, text="")
result_animal.pack()

root.mainloop()