from tkinter import *
root =Tk()
root.geometry("700x400")

def hello():
    print("HELLO all my TEAMMATES & HOW ARE U & HOPE U R QUARENTINING WELL")
def name():
    print("My Name is ARSH SETH")

frame=Frame(root, borderwidth=6,bg="grey",relief=SUNKEN)
frame.pack(side=LEFT,anchor="ne")

b1=Button(frame,fg="red",text="HELLO AYUSHI",command=hello)
b1.pack(side=LEFT,padx=3)

b2=Button(frame,fg="red",text="TELL me MY name now", command=name)
b2.pack(side=LEFT,padx=23)

b3=Button(frame,fg="green",text="DIWALI")
b3.pack(side=LEFT,padx=23)

b4=Button(frame,fg="purple",text="HOLI")
b4.pack(side=LEFT,padx=23)

b5=Button(frame,fg="orange",text="CHRISTMAS")
b5.pack(side=LEFT,padx=23)


root.mainloop()