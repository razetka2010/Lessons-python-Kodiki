from tkinter import *

root = Tk() 
root.geometry("300x200")

label = Label(root, text="Привет! Это моё окно")
label.pack()

def anecdote():
    label.config(text="- Блин! – сказал слон, наступив на Колобка.")

Joke = Button(root, text="Шутка", command=anecdote)
Joke.pack()

def initial():
    label.config(text="Привет! Это моё окно")

Elementary = Button(root, text="Начальный текст", command=initial)
Elementary.pack()
    
root.mainloop()
