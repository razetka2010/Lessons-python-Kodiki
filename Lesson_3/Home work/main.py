from tkinter import *

root = Tk()
root.title("Калькулятор")
root.geometry("300x300")

def add(): #Сложение
    a = int(entry1.get())
    b = int(entry2.get())
    label_result.config(text=f"Результат: {a + b}")

def subtract(): #Вычитание
    a = int(entry1.get())
    b = int(entry2.get())
    label_result.config(text=f"Результат: {a - b}")

def multiply(): #Умножение
    a = int(entry1.get())
    b = int(entry2.get())
    label_result.config(text=f"Результат: {a * b}")

def share(): #Деление
    a = int(entry1.get())
    b = int(entry2.get())
    label_result.config(text=f"Результат: {a / b}")

def division_omplete(): #Деление нацело
    a = int(entry1.get())
    b = int(entry2.get())
    label_result.config(text=f"Результат: {a // b}")

def remainder_division(): #Остаток от деления
    a = int(entry1.get())
    b = int(entry2.get())
    label_result.config(text=f"Результат: {a % b}")

def exponentiation(): #Возведение в степень
    a = int(entry1.get())
    b = int(entry2.get())
    label_result.config(text=f"Результат: {a ** b}")

label_result = Label(root, text="Результат: 0")
label_result.pack()

entry1 = Entry(root)
entry1.pack(pady=5)

entry2 = Entry(root)
entry2.pack(pady=5)

button_add = Button(root, text="Сложить", command=add)
button_add.pack()

button_subtract = Button(root, text="Вычесть", command=subtract)
button_subtract.pack()

button_multiply = Button(root, text="Умножить", command=multiply)
button_multiply.pack()

button_share = Button(root, text="Делить", command=share)
button_share.pack()

button_division_omplete = Button(root, text="Делить нацело", command=division_omplete)
button_division_omplete.pack()

button_remainder_division = Button(root, text="Остаток от деления", command=remainder_division)
button_remainder_division.pack()

button_exponentiation = Button(root, text="Возведение в степень", command=exponentiation)
button_exponentiation.pack()

root.mainloop()
