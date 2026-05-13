from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.geometry('400x500')
root.title("Моё окно")
root.config(bg='#d2c3d5')

img = PhotoImage(file="artempog3.png")
label1 = Label(root, image=img, bg="#000000", fg="#FFFFFF", text="Артём с Илоном Маском", compound="top")
label1.pack(pady=20)

img1 = Image.open("artempog4.jpg")
img1 = img1.resize((200, 200))
photo = ImageTk.PhotoImage(img1)

label = Label(root, image=photo, text="Артём со Сталиным", compound="top", bg="#000000", fg='#FFFFFF')
label.pack(pady=20)

root.mainloop()