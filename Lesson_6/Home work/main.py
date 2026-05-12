from tkinter import *

root = Tk()
root.geometry("400x300")
root.title("Моё окно")

label = Label(root, text="Шитиков", fg="Blue", font=("Comiv Sans SM", 18, "underline"))
label.pack(pady=5)

label = Label(root, text="Артём", fg="green", font=("Times New Roman", 20))
label.pack(pady=5)

root.mainloop()
