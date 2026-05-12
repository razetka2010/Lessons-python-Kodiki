from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("500x300")
root.title("Мини-викторина")
root.config(bg="#65b8aa")

quiz = [
    {"text": "Ты пог или пог?",
     "options": ["пог", "не я не пог", "пог", "хз"],
      "answer": 0},
    {"text": "Какая Oc лучше?",
      "options": ["Winda", "Mac Oc",
      "Linux"], "answer": 1},
    {"text": "Max крутое приложение?",
      "options": ["Да", "Конечно", "Нет", "фигня"],
      "answer": 2}
]

i = 0
score = 0
choice = IntVar(value=-1)

def show_question():
    q = quiz[i]
    q_label.config(text=f"Вопрос {i+1} / {len(quiz)}: {q['text']}")

    for w in opts.winfo_children():
        w.destroy()

    choice.set(-1)

    for idx, text in enumerate(q["options"]):
        Radiobutton(opts, text=text, variable=choice, value=idx,
            bg="#65b8aa",
            anchor="w", font=("Arial", 12, "bold")).pack(fill="x", padx=12, pady=2)
        
    btn_next.config(text="Завершить" if i == len(quiz) - 1 else "Далее")
    status.config(text="Сделайте выбор и нажмите Далее. ")

def next_questions():
    global i
    if i < len(quiz) - 1:
        i += 1
        show_question()
    else:
        q_label.config(text="Викторина завершина!", )
        for w in opts.winfo_children():
            w.destroy()
        btn_next.config(state="disabled")

def check_end_go():
    global i, score
    sel = choice.get()
    if sel == -1:
        messagebox.showwarning("Викторина", "Сначала выбирите вариант!", parent=root)
        return
    
    if sel == quiz[i]["answer"]:
        score += 1
        status.config(text="Верно!")
    else:
        right_text = quiz[i]["options"][quiz[i]["answer"]]
        status.config(text=f"Неверно. Правильный ответ: {right_text}")

    if i < len(quiz) - 1:
        i += 1
        root.after(400, show_question)
    else:
        show_result()

def show_result():
    percent = round(score / len(quiz) * 100)
    messagebox.showinfo("Результат",
                        f"Правильных ответов: {score} из {len(quiz)} ({percent}%)",
                        parent=root)
    
    again = messagebox.askyesno("Викторина", "Сыграть ещё раз?", parent=root)
    if again:
        restart()
    else:
        root.destroy

def restart():
    global i, score
    i = 0
    score = 0
    status.config(text="")
    show_question()

q_label = Label(root, text="", font=("Arial", 14), bg="#65b8aa", fg="#ffffff")
q_label.pack(pady=6)

opts = Frame(root, bg="#65b8aa")
opts.pack(pady=6)

status = Label(root, text="", font=("Arial", 10), bg="#65b8aa", fg="#ffffff")
status.pack(pady=4)

btn_next = Button(root, text="Далее", font=("Arial", 12), bg="#970372", fg="#ffffff")
btn_next.pack(pady=10)

btn_next.config(command=next_questions)
btn_next.config(command=check_end_go)
show_question()

root.mainloop() 