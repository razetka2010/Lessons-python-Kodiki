from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.geometry('600x400')
root.title("Моё окно")
root.config(bg='#d2c3d5')

img = PhotoImage(file="artempog.png")
label1 = Label(root, image=img, bg='#d2c3d5',)
label1.pack(pady=20)

img1 = Image.open("artempog2.jpg")
img1 = img1.resize((150, 100))
photo = ImageTk.PhotoImage(img1)

label = Label(root, image=photo)
label.pack(pady=20)

root.mainloop()