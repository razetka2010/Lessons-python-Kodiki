from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("400x250")
root.title("Опрос")
root.config(bg="lightgreen")

questions = [
    {"text": "Какой ваш любимый цвет?", "options": ["Красный", "Синий", "Зелёный", "Жёлтый", "Пог"]},
    {"text": "Что вам больше нравится?", "options": ["Кино0", "Книги", "Игры", "Спорт"]},
    {"text": "Какое животное вам ближе?", "options": ["Кошка", "Собака", "Птица", "Рыбка"]},
    {"text": "Вы Пог или Пог", "options": ["Пог", "Не  пог", "Пог", "Пог", "Пог", "Пог", "Пог"]}                                                                                             
]

def show_questions():
    q = questions[i]
    q_label.config(text=f"Вопрос {i+1}: {q['text']}")

    for w in opts.winfo_children():
        w.destroy()

    chose.set(-1)

    for idx, text in enumerate(q["options"]):
        Radiobutton(opts, text=text, variable=chose, value=idx).pack(anchor="w")
    
    btn.config(text="Завершить" if i == len(questions)-1 else "Далее")

def next_or_fiish():
    global i
    if chose.get() == -1:
        messagebox.showwarning("Опрос", "Выерите!", parent=root)
        return
    if i < len(questions) - 1:
        i += 1
        show_questions()
    else:
        messagebox.showwarning("Опрос", "Спасибо за участие!", parent=root)
        root.destroy()

i = 0
chose = IntVar(master=root, value=-1)

q_label = Label(root, text="", font=("Arial", 14))
q_label.pack(pady=10)

opts = Frame(root, bg="#87CEEB")
opts.pack()

btn = Button(root, text="Далее", font=("Arial", 12), command=next_or_fiish)
btn.pack(pady=12)

show_questions()

root.mainloop()