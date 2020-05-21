from tkinter import *
root = Tk()
root.geometry("700x500")
f1=Frame(root,bg="skyblue", borderwidth=14,relief=SUNKEN)
f1.pack(side=LEFT,fill="y")

f2=Frame(root,bg="skyblue", borderwidth=15,relief=SUNKEN)
f2.pack(side=TOP,fill="x")

l= Label(f1,text="PROJECT BY - MR.ARSH SETH== Pycharm")
l.pack(pady=142)

l= Label(f2,text="WELCOME to SUBLIME TEXT",font="Helvetica 16 bold",fg ="blue",pady=22)
l.pack(pady=42)


root.mainloop()
