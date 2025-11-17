from tkinter import *
from tkinter import messagebox

root=Tk()
root.geometry("400x300")
root.title("Message Box Example")

def show_warning():
    messagebox.showwarning("Alert", "virus detected")
Btn=Button(root,text="Click Me",command=show_warning)
Btn.pack()
root.mainloop()



