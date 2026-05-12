from tkinter import *

root = Tk()
root.geometry("500x500")
root.title("Список")

pokupki = []

def add_task():
    text = entry.get().strip()
    if text:
        pokupki.append(text)
        listbox.insert(END, text)
        print("Добавил: ", text)
        entry.delete(0, END)

def delete_tasks():
        listbox.delete(0, END)

label = Label(root, text="Список продуктов", font=("bold"))
label.pack(pady=5)

entry = Entry(root, width=28)
entry.pack(pady=6)

btn_add = Button(root, text="Добавить", command=add_task)
btn_add.pack(pady=4)

listbox = Listbox(root, width=34, height=10)
listbox.pack(pady=6)

dlt_add = Button(root, text="Очистить всё", command=delete_tasks)
dlt_add.pack(pady=6)

root.mainloop()
