from tkinter import *
def getvals():
    print(f"The value of username is {uservalue.get()}")
    print(f"The value of passname is {passvalue.get()}")
root=Tk()
root.geometry("400x300")
root.title("FORM FOR CRICKET TRIAL ENTRIES")

User=Label(root,text="USERNAME")
Password= Label(root,text="PASSWORD")
User.grid()
Password.grid(row=1)

#Variable classes in Tkinter
# BooleanVar,DoubleVar,IntVar,StringVar

uservalue = StringVar()
passvalue = StringVar()

userentry = Entry (root, textvariable = uservalue)
passentry = Entry (root, textvariable = passvalue)

userentry.grid(row=0,column=1)
passentry.grid(row=1,column=1)

Button(text="SUBMIT",command=getvals).grid()

root.mainloop()