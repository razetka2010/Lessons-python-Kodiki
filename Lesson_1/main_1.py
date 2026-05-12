from tkinter import *

root = Tk()
root.geometry("300x400")

lambel = Label(root, text="Это текст")
lambel.pack()

def cange_text():
    lambel.config(text="Ты нажал на кнопку!")

button = Button(root, text="Нажми на меня", command=cange_text)
button.pack()

root.mainloop()