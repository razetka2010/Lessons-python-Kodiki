from tkinter import *

root = Tk()
root.title("Калькулятор")
root.geometry("300x250")

def add():
    a = int(entry1.get())
    b = int(entry2.get())
    label_result.config(text=f"Результат: {a + b}")

def subtract():
    a = int(entry1.get())
    b = int(entry2.get())
    label_result.config(text=f"Результат: {a - b}")

entry1 = Entry(root)
entry1.pack(pady=5)

entry2 = Entry(root)
entry2.pack(pady=5)

button_add = Button(root, text="Сложить", command=add)
button_add.pack()

button_subtract = Button(root, text="Вычесть", command=subtract)
button_subtract.pack()

label_result = Label(root, text="Результат:")
label_result.pack()

root.mainloop()