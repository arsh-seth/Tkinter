

from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("700x500")
root.title("Radiobutton tutorial")

def order():

    tmsg.showinfo("Order Received!", f"We have received your order for {var.get()}. Thanks for ordering")

def getdollar():
        print(f"We have credited {myslider2.get()} dollars to your bank account")
        tmsg.showinfo("Amount Credited!", f"We have credited {myslider2.get()} dollars to your bank account")


# var = IntVar()
var = StringVar()
var.set("Radio")
# var.set(1)
Label(root, text = "What would you like to have SIR in ARSH's HOTEL ?",font="lucida 19 bold",
      justify=LEFT, padx=14).pack()

Label(root, text="How many dollars do you want?").pack()
myslider2 = Scale(root, from_=0, to=100, orient=HORIZONTAL, tickinterval=50)
    # myslider2.set(34)
myslider2.pack()

Button(root, text="Get dollars!", pady=10, command=getdollar).pack()

Label(root, text="GET YOUR DISHES BELOW?",font="comicsansms 9 ").pack()


radio = Radiobutton(root, text="Dosa", padx=14, variable=var, value="Dosa").pack(anchor="w")
radio = Radiobutton(root, text="Idly", padx=14, variable=var, value="Idly").pack(anchor="w")
radio = Radiobutton(root, text="Paratha", padx=14, variable=var, value="Paratha").pack(anchor="w")
radio = Radiobutton(root, text="Samosa", padx=14, variable=var, value="Samosa").pack(anchor="w")

Button(text="Order HERE", command=order).pack()
root.mainloop()
