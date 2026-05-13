from tkinter import *
from PIL import Image, ImageTk
import os
from tkinter import filedialog

root = Tk()
root.geometry("800x600")
root.title("Фото-галерея")
root.config(bg="#d2c3d5")

images = []
index = 0
btn_prev = None
btn_next = None

def open_folder():
    global images, index
    folder = filedialog.askdirectory()
    if not folder:
        return
    
    files = os.listdir(folder)
    images = []
    
    for f in files:
        if f.lower().endswith((".png", ".jpeg", ".gif", ".jpg")):
            full_path = os.path.join(folder, f)
            images.append(full_path)
    
    index = 0
    if images:
        show_image()
        btn_open.pack_forget()
        create_nav_button()

def show_image():
    global index
    if not images:
        return
    img = Image.open(images[index])
    img.thumbnail((600, 400))
    photo = ImageTk.PhotoImage(img)
    label.config(image=photo)
    label.image = photo

def next_image():
    global index
    if index < len(images) - 1:
        index += 1
        show_image()
    
def prev_image():
    global index
    if index > 0:
        index -= 1
        show_image()

controls = Frame(root, bg="#d2c3d5")
controls.pack(pady=10)

def load_png(path, size=(100, 100)):
    if os.path.exists(path):
        img = Image.open(path)
        img = img.resize(size)
        return ImageTk.PhotoImage(img)
    return None

label = Label(root, bg="#d2c3d5")
label.pack(pady=20)

img_prev = load_png("prev.png")
img_next = load_png("next.png")
img_open = load_png("open.png")

def create_nav_button():
    global btn_next, btn_prev
    
    # Создаем кнопки если их еще нет
    if btn_prev is None:
        btn_prev = Button(controls, image=img_prev, command=prev_image, bg="#d2c3d5", activebackground="#ffe8ad")
        btn_prev.pack(side=LEFT, padx=10)

    if btn_next is None:
        btn_next = Button(controls, image=img_next, command=next_image, bg="#d2c3d5", activebackground="#ffe8ad")
        btn_next.pack(side=LEFT, padx=10)

btn_open = Button(controls, image=img_open, command=open_folder, bg="#d2c3d5", activebackground="#ffe8ad")
btn_open.pack(pady=10)

root.mainloop()