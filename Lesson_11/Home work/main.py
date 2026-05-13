from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.geometry('950x400')
root.title("Моё окно")
root.config(bg='#d2c3d5')

krasota1 = Image.open("Krasota1.jpg").resize((300, 200))
krasota2 = Image.open("Krasota2.jpg").resize((300, 200))
krasota3 = Image.open("Krasota3.jpg").resize((300, 200))

photo1 = ImageTk.PhotoImage(krasota1)
photo2 = ImageTk.PhotoImage(krasota2)
photo3 = ImageTk.PhotoImage(krasota3)

frame_jpg = Frame(root, bg='#d2c3d5')
frame_jpg.pack(pady=10)

label1 = Label(frame_jpg, image=photo1, bg='#d2c3d5')
label1.pack(side=LEFT, padx=5)

label2 = Label(frame_jpg, image=photo2, bg='#d2c3d5')
label2.pack(side=LEFT, padx=5)

label3 = Label(frame_jpg, image=photo3, bg='#d2c3d5')
label3.pack(side=LEFT, padx=5)

krasota4 = Image.open("Krasota4.png").resize((300, 200))
krasota5 = Image.open("Krasota5.png").resize((300, 200))
krasota6 = Image.open("Krasota6.png").resize((300, 200))

krasota41 = ImageTk.PhotoImage(krasota4)
krasota52 = ImageTk.PhotoImage(krasota5)
krasota63 = ImageTk.PhotoImage(krasota6)

frame1 = Frame(root, bg='#d2c3d5')
frame1.pack(pady=10)

label4 = Label(frame1, image=krasota41, bg='#d2c3d5')
label4.pack(side=LEFT, padx=5)

label5 = Label(frame1, image=krasota52, bg='#d2c3d5')
label5.pack(side=LEFT, padx=5)

label6 = Label(frame1, image=krasota63, bg='#d2c3d5')
label6.pack(side=LEFT, padx=5)

root.mainloop()