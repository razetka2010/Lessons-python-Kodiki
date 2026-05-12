from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("300x350")
root.title("Messagebox Demo")

def show_info():
    messagebox.showinfo('Инфо', 'Это информационное сообщение!')

def show_warn():
    messagebox.showwarning('Предупреждение', 'Это предупреждающее сообщение!')

show_info()
show_warn()

root.mainloop()