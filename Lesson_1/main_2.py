from tkinter import *

root = Tk()
root.geometry("500x250")

label = Label(root, text="Привет! Выбери действие нажав на кнопку")
label.pack()

def Pog01():
    label.config(text="Африка — единственный континент, который находится во всех четырёх полушариях Земли.")

Pog = Button(root, text="Факт 1", command=Pog01)
Pog.pack()

def Pog02():
    label.config(text="У белых медведей чёрная кожа и прозрачная шерсть.")

Pog1 = Button(root, text="Факт 2", command=Pog02)
Pog1.pack()

root.mainloop()