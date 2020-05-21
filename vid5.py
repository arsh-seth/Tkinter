# display image and text
from tkinter import *
from PIL import Image, ImageTk

disp_root = Tk()

disp_root.geometry("555x333")
ARSH = Label(text="ARSH is a good Boy & This is his GUI")
ARSH.pack()
# photo = PhotoImage(file="1.png")

# For Jpg Images


image = Image.open("photo.jpg.jpg")    # use any photo namely photo.jpg.jpg or of your choice
photo = ImageTk.PhotoImage(image)

arsh_label = Label(image=photo)
arsh_label.pack()


disp_root.mainloop()




