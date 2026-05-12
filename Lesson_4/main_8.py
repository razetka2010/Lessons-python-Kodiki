from tkinter import *
import time

root = Tk()
root.geometry("300x200")
root.title("Секундамер")

running = False
start_time = 0.0
after_id = None

def update():
    global after_id
    time_passed = time.perf_counter() - start_time
    minutes = int(time_passed // 60)
    second = int(time_passed % 60)
    parts_hundred = int((time_passed - int(time_passed)) * 100)
    time_label.config(text=f"{minutes:02d}:{second:02d}.{parts_hundred:02d}")
    after_id = root.after(10, update)

def switch():
    global running, start_time, after_id
    if running:
        running = False
        if after_id:
            root.after_cancel(after_id)
            after_id = None
        button_start.config(text="Старт")
    else:
        running = True
        start_time = time.perf_counter()
        update()
        button_start.config(text="Стоп")

def reset():
    global running, after_id
    running = False
    if after_id:
        root.after_cancel(after_id)
        after_id = None
    time_label.config(text="00:00:00")
    button_start.config(text="Старт")

time_label  = Label(root, text="00:00:00", font=24)
time_label.pack(pady=20)

button_start = Button(root, text="Старт", command=switch)
button_start.pack(padx=10, pady=5)

button_reset = Button(root, text="Сброс", command=reset)
button_reset.pack(padx=10, pady=5)

root.mainloop()