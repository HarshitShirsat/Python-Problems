from tkinter import *
from tkinter import messagebox

def display():
    ia=int(t1.get())
    y=int(t2.get())
    air=float(t3.get())
    mir=air/1200
    c=ia*(1+mir)**(y*12)
    l5.configure(text=str(c))

window=Tk()
l1=Label(window,text="Investment Amount")
l1.grid(column=10,row=0)
t1=Entry(window)
t1.grid(column=20,row=0)
l2=Label(window,text="Years")
l2.grid(column=10,row=1)
t2=Entry(window)
t2.grid(column=20,row=1)
l3=Label(window,text="Annual Interest Rate")
l3.grid(column=10,row=2)
t3=Entry(window)
t3.grid(column=20,row=2)
l4=Label(window,text="Future Value")
l4.grid(column=10,row=3)
l5=Label(window,text="....")
l5.grid(column=20,row=3)
b1=Button(window,text="Calculate",command=display)
b1.grid(column=15,row=4)
window.mainloop()
