from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("300x350")
root.title("Messagebox Demo")

def ask_yesno():
    ask = messagebox.askquestion("Привет", "Хочешь поздороваться?")

    if ask == "yes":
        messagebox.showinfo("Ответ", "Привет, друг!")
    else:
        messagebox.showwarning("Ответ", "Ну ладно, может в следующий раз!")

ask_yesno()

root.mainloop()