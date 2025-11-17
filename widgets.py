from tkinter import *
root = Tk()
root.geometry("400x300")
root.title("main")

def topwin():
    top = Toplevel()
    top.geometry("100x100")
    top.title("top")
    
    label=Label(top,text="this is top window")
    label.pack()
    top.mainloop()
btn =Button(root,text="click me ",command=topwin)
btn.pack()
root.mainloop()



 

