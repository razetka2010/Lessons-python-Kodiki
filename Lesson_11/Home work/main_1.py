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

index = 0

pog = Image.open(img[index])
pog1 = pog.resize((300, 200))
pog2 = ImageTk.PhotoImage(pog1)

image_label = Label(root, image=pog2, bg='#d2c3d5')
image_label.pack(pady=20)

root.mainloop()