from tkinter import *
import random
import string

root = Tk()
root.geometry("400x250")
root.title("генератор паролей")

def generator_password():
    lenght = int(entry.get())
    lett = list(string.ascii_letters)
    di = list(string.digits)
    punct = list(string.punctuation)
    all_chars = lett + di + punct
    pasword_list = random.choices(all_chars, k=lenght)
    password = ''.join(pasword_list)
    result_label.config(text=f"Пароль: {password}")

label = Label(root, text="Генератор паролей")
label.pack(pady=10)

label2 = Label(root, text="Введите длину пароля")
label2.pack(pady=5)

entry = Entry(root)
entry.pack(pady=10)

button = Button(root, text="Сгенерировать пароль", command=generator_password)
button.pack(pady=10)

result_label = Label(root, text="Пароль появится тут")
result_label.pack(pady=5)

root.mainloop()