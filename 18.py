from tkinter import *
from tkinter import messagebox

def sum():
    a=int(t1.get())
    b=int(t2.get())
    c=a+b
    messagebox.showinfo("SUM","Sum is "+str(c))

window=Tk()
l1=Label(window,text="Enter number 1")
l1.pack()
t1=Entry(window)
t1.pack()
l2=Label(window,text="Enter number 2")
l2.pack()
t2=Entry(window)
t2.pack()
b1=Button(window,text="Sum",command=sum)
b1.pack()
window.mainloop()
