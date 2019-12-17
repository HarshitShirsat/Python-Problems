from tkinter import *
from tkinter import messagebox

def add():
    a=int(t1.get())
    b=int(t2.get())
    c=a+b
    messagebox.showinfo("SUM","Sum is "+str(c))

def subtract():
    a=int(t1.get())
    b=int(t2.get())
    c=a-b
    messagebox.showinfo("DIFFERENCE","Difference is "+str(c))

def multiply():
    a=int(t1.get())
    b=int(t2.get())
    c=a*b
    messagebox.showinfo("PRODUCT","Product is "+str(c))

def divide():
    a=int(t1.get())
    b=int(t2.get())
    c=a/b
    messagebox.showinfo("QUOTIENT","Quotient is "+str(c))

window=Tk()
l1=Label(window,text="Enter number 1")
l1.grid(column=10,row=0)
t1=Entry(window)
t1.grid(column=20,row=0)
l2=Label(window,text="Enter number 2")
l2.grid(column=10,row=1)
t2=Entry(window)
t2.grid(column=20,row=1)
b1=Button(window,text="Add",command=add)
b1.grid(column=5,row=2)
b2=Button(window,text="Subtract",command=subtract)
b2.grid(column=10,row=2)
b3=Button(window,text="Multiply",command=multiply)
b3.grid(column=15,row=2)
b4=Button(window,text="Divide",command=divide)
b4.grid(column=20,row=2)
window.mainloop()
