from tkinter import *

root = Tk()
root.title("Ввод данных")
root.geometry("300x200")

label = Label(root, text=" ")
label.pack()

entry = Entry(root)
entry.pack()

def show_text():
    user_text = entry.get()
    label.config(text=f"Ты написал вот это: {user_text}")

button = Button(root, text="Показать", command=show_text)
button.pack()

root.mainloop()