from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("300x350")
root.title("Messagebox Demo")

def show_info():
    messagebox.showinfo('Инфо', 'Это информационное сообщение!')

def show_warn():
    messagebox.showwarning('Предупреждение', 'Это предупреждающее сообщение!')

def show_err():
     messagebox.showerror('Ошибка', 'Ой, внимание ошиюка!')

def ask_yesno():
    ask = messagebox.askyesno('Да или нет?', 'Выбирай пж')
    print('Ответ на yes/no: ', ask)

def ask_quetion():
    ask = messagebox.askquestion('Вопрос', 'Ты готов начать игру?')
    print('Ответ на quetion: ', ask)

button1 = Button(text='Инфо', command=show_info)
button1.pack()

button2 = Button(text='Предупреждение', command=show_warn)
button2.pack

button3 = Button(text='Ошибка', command=show_err)
button3.pack()

button4 = Button(text='Да/Нет', command=ask_yesno)
button4.pack()

button5 = Button(text='Вопрос', command=ask_quetion)
button5.pack()

root.mainloop()