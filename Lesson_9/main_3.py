from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.geometry('800x600')
root.title("Тест изображения")
root.config(bg='#d2c3d5')
# 
# gif = []
# for i in range(15):
#     frame = PhotoImage(file="2.gif", format=f"gif - {i}")
#     gif.append(frame)

# def play(i = 0):
#     label.config(image=gif[i])
#     root.after(100, play, (i+1) % len(gif))

# img = PhotoImage(file="1.png")
# label = Label(root, image=img, bg='#d2c3d5')
# label.pack(pady=20)
# 
# label = Label(root, bg="#d2c3d5")
# label.pack()

# play()

img = Image.open("2.jpg")
img = img.resize((300, 300))
photo = ImageTk.PhotoImage(img)

label = Label(root, image=photo, text="Первая картинка", compound="top")
label.pack(pady=20)

root.mainloop()
