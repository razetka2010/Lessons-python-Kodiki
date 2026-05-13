from tkinter import *

root = Tk()
root.geometry('600x500')
root.title("Тест изображения")
root.config(bg='#d2c3d5')

gif = []
gif1 = []

for i in range(15):
    frame = PhotoImage(file="2.gif", format=f"gif - {i}")
    frame = frame.subsample(2, 2)
    gif.append(frame)

def play(i = 0):
    label.config(image=gif[i])
    root.after(100, play, (i+1) % len(gif))

for a in range(15):
    frame2 = PhotoImage(file="1.gif", format=f"gif - {a}")
    frame2 = frame2.subsample(2, 2)
    gif1.append(frame2)

def play1(a = 0):
    label2.config(image=gif1[a])
    root.after(100, play1, (a+1) % len(gif1))    

label = Label(root, bg="#d2c3d5")
label.pack(pady=10)

label2 = Label(root, bg="#d2c3d5")
label2.pack(pady=10)

play()
play1()

root.mainloop()