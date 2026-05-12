from tkinter import *

root = Tk()
root.geometry("500x500")
root.title("Дни недели")

def delete_tasks():
    sel = listbox.curselection()
    if sel:
        i = sel[0]
        listbox.delete(i)
        
label = Label(root, text="Дни делели")
label.pack(pady=5)

listbox = Listbox(root)
listbox.pack(pady=5)

listbox.insert(END, "Понедельник")
listbox.insert(END, "Вторник")
listbox.insert(END, "Среда")
listbox.insert(END, "Четверг")
listbox.insert(END, "Пятница")
listbox.insert(END, "Суббота")
listbox.insert(END, "Воскресенье")

dlt_add = Button(root, text="Удалить", command=delete_tasks)
dlt_add.pack(pady=6)

root.mainloop()