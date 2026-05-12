from tkinter import *

root = Tk()
root.geometry("500x500")
root.title("Цвета и шрифты")
root.config(bg="#00c8ff")

label = Label(root, text="Привет, tkinter", fg="red", bg="yellow")
label.pack(pady=20)

label = Label(root, text="Пог", font=("Arial", 16, "bold"))
label.pack(pady=10)

label = Label(root, text="Пог", font=("Courier New", 17, "italic"))
label.pack(pady=10)

label = Label(root, text="Пог", font=("Comiv Sans SM", 18, "underline"))
label.pack(pady=10)

label = Label(root, text="Пог", font=("Times New Roman", 20))
label.pack(pady=10)

label = Label(root, text="Пог", fg="green", bg="yellow", font=("Arial", 17, "bold"))
label.pack(pady=5)

label = Label(root, text="Пог", fg="#ff9900", bg="#c800ff", font=("Courier New", 20, "italic"))
label.pack(pady=5)

root.mainloop()