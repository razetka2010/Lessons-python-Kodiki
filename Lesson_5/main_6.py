from tkinter import *

root = Tk()
root.geometry("400x340")
root.title("Список дел")
root.config(bg="#aa00ff")

tasks = []

title = Label(root, text="Мои задачи")
title.pack(pady=8)

entry = Entry(root, width=28)
entry.pack(pady=6)

def add_task():
    text = entry.get().strip()
    if text:
        tasks.append(text)
        listbox.insert(END, text)
        print("Добавил: ", text)
        entry.delete(0, END)

def delete_tasks():
    sel = listbox.curselection()
    if sel:
        i = sel[0]
        listbox.delete(i)
        tasks.pop(i)

btn_add = Button(root, text="Добавить", command=add_task)
btn_add.pack(pady=4)

listbox = Listbox(root, width=34, height=10)
listbox.pack(pady=6)

dlt_add = Button(root, text="Удалить", command=delete_tasks)
dlt_add.pack(pady=6)

root.mainloop()