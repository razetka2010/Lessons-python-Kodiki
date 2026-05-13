from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.geometry('600x400')
root.title("Моё окно")
root.config(bg='#d2c3d5')

img = [
    "Krasota1.jpg",
    "Krasota2.jpg", 
    "Krasota3.jpg",
    "Krasota4.png",
    "Krasota5.png",
    "Krasota6.png"
]

def show_image():
    global pog2
    pog = Image.open(img[index])
    pog1 = pog.resize((300, 200))
    pog2 = ImageTk.PhotoImage(pog1)
    image_label.config(image=pog2)

def next_image():
    global index
    if index < len(img) - 1:
        index += 1
        show_image()

def prev_image():
    global index
    if index > 0:
        index -= 1
        show_image()

index = 0

pog = Image.open(img[index])
pog1 = pog.resize((300, 200))
pog2 = ImageTk.PhotoImage(pog1)

image_label = Label(root, image=pog2, bg='#d2c3d5')
image_label.pack(pady=20)

frame = Frame(root, bg='#d2c3d5')
frame.pack()

prev = Button(frame, text="Назад", command=prev_image)
prev.pack(side=LEFT, padx=10)

next = Button(frame, text="Вперед", command=next_image)
next.pack(side=LEFT, padx=10)

show_image()
root.mainloop()