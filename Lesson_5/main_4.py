from  tkinter import *

root = Tk()

def updete():
    print("Привет это задержка в 2 секунды")
    root.after(2000, updete)

updete()

root.mainloop()