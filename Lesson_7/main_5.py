from tkinter import *

root = Tk()
root.geometry("500x350")
root.title("Игра викторина")

quiz = [
    {"text": "Как в Python начинается список?", "options": ["()", "[]", "{}", "<>"]},
    {"text": "Какая функция в Python выводит данные на экран?", "options": ["input()", "print()", "len()", "type()"]},
    {"text": "Столица Китая", "options": ["Бангкок", "Пекие", "Сингапур", "Сеул"]}
]

i = 0
choise = IntVar(value=-1)

def show_question():
    q = quiz[i]
    q_label.config(text=f"Вопрос {i+1} / {len(quiz)}: {q['text']}")

    for w in opts.winfo_children():
        w.destroy()

    choise.set(-1)

    for idx, text in enumerate(q["options"]):
        Radiobutton(opts, text=text, variable=choise, value=idx,
            anchor="w", font=("Arial", 12)).pack(fill="x", padx=12, pady=2)
        
    btn_next.config(text="Завершить" if i == len(quiz) - 1 else "Далее")

def next_question():
    global i
    if i < len(quiz) - 1:
        i += 1
        show_question()
    else:
        q_label.config(text="Викторина завершина!")
        for w in opts.winfo_children():
            w.destroy()
        btn_next.config(state="disabled")

label = Label(text="Игра викторина", font=("Arial", 20, "bold"))
label.pack(pady=8)

q_label = Label(root, text="", font=("Arial", 14))
q_label.pack(pady=6)

opts = Frame(root)
opts.pack(pady=6)

btn_next = Button(root, text="Далее", font=("Arial", 12))
btn_next.pack(pady=10)

btn_next.config(command=next_question)
show_question()

root.mainloop()